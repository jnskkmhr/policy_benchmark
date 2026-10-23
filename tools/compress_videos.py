"""Compress exported videos without modifying the original benchmark recordings."""

import argparse
import hashlib
import json
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIMIT = 20_000_000


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def probe(path):
    result = subprocess.check_output(
        [
            "ffprobe",
            "-v",
            "error",
            "-select_streams",
            "v:0",
            "-show_entries",
            "stream=width,height,r_frame_rate,nb_frames:format=duration",
            "-of",
            "json",
            str(path),
        ]
    )
    info = json.loads(result)
    return info["streams"][0], float(info["format"]["duration"])


def compress(target, source_root, previous):
    relative = target.relative_to(ROOT / "videos")
    source = source_root / relative
    if source.resolve() == target.resolve():
        raise ValueError("Original recordings must be outside the export directory")
    source_hash = digest(source)
    key = str(target.relative_to(ROOT))
    old = previous.get(key)
    if (
        old
        and old["source_sha256"] == source_hash
        and old["published_sha256"] == digest(target)
    ):
        return key, old
    stream, duration = probe(source)
    max_rate = min(
        4_000_000 if stream["width"] > 1000 else 2_000_000,
        int(16_000_000 * 8 / duration),
    )
    temporary = target.with_suffix(".tmp.mp4")
    try:
        subprocess.run(
            [
                "ffmpeg",
                "-v",
                "error",
                "-y",
                "-i",
                str(source),
                "-map",
                "0:v:0",
                "-an",
                "-c:v",
                "libx264",
                "-preset",
                "medium",
                "-crf",
                "24",
                "-threads",
                "2",
                "-maxrate",
                str(max_rate),
                "-bufsize",
                str(max_rate * 2),
                "-pix_fmt",
                "yuv420p",
                "-fps_mode",
                "passthrough",
                "-movflags",
                "+faststart",
                str(temporary),
            ],
            check=True,
        )
        output_stream, output_duration = probe(temporary)
        if output_stream != stream or abs(output_duration - duration) > 0.001:
            raise RuntimeError(f"Video timing or dimensions changed: {target}")
        if temporary.stat().st_size >= LIMIT:
            raise RuntimeError(f"Compressed video exceeds 20 MB: {target}")
        record = {
            "source_sha256": source_hash,
            "published_sha256": digest(temporary),
            "source_bytes": source.stat().st_size,
            "published_bytes": temporary.stat().st_size,
            "duration_s": duration,
            **stream,
        }
        temporary.replace(target)
        return key, record
    finally:
        temporary.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "source",
        type=Path,
        help="Directory containing original videos, with matching relative paths",
    )
    parser.add_argument("--jobs", type=int, default=4)
    args = parser.parse_args()
    manifest_path = ROOT / "video_compression.json"
    records = (
        json.loads(manifest_path.read_text())["videos"]
        if manifest_path.exists()
        else {}
    )
    videos = sorted((ROOT / "videos").rglob("*.mp4"))
    videos = [path for path in videos if not path.name.endswith(".tmp.mp4")]
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futures = [pool.submit(compress, path, args.source, records) for path in videos]
        for count, future in enumerate(as_completed(futures), 1):
            key, record = future.result()
            records[key] = record
            manifest_path.write_text(
                json.dumps(
                    {
                        "max_bytes_exclusive": LIMIT,
                        "codec": "H.264",
                        "faststart": True,
                        "resolution_fps_frame_count_and_duration_preserved": True,
                        "videos": dict(sorted(records.items())),
                    },
                    indent=2,
                )
                + "\n"
            )
            print(
                f"{count}/{len(videos)} {key}: {record['source_bytes']} -> {record['published_bytes']} bytes",
                flush=True,
            )

    live_path = ROOT / "live.json"
    live = json.loads(live_path.read_text())
    live["video_versions"] = {
        str(path.relative_to(ROOT)): str(path.stat().st_mtime_ns) for path in videos
    }
    live_path.write_text(json.dumps(live, indent=2) + "\n")


if __name__ == "__main__":
    main()
