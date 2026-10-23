# Private policy benchmark

Live results for four G1 policies, six MPM Play tasks, and three materials.

Open `index.html` through an HTTP server. On the simulation machine:

```bash
python3 -m http.server 8765 --bind 127.0.0.1 --directory /home/jkamohara/isaac/policy_benchmark
```

In VS Code connected over SSH, open **Ports → Forward a Port → 8765**, then open the forwarded address.
The server listens only on localhost. Do not publish this repository with public GitHub Pages.

The page refreshes results every 30 seconds. New completed rollouts are exported and pushed periodically while the benchmark runs.
Checkpoint weights and W&B credentials are excluded.

[Full report](data/four_policy_20261022_v3/report.md) · [Raw measurement table](data/four_policy_20261022_v3/summary.csv)

Each task's report includes individual and 2×2 videos, PNG/PDF figures, and measurement definitions.
Early task terminations and solver failures remain visible. This is one episode per condition at seed 42.

Completed: **72 primary recordings**, **3 separate capacity-check reruns**, and **18 time-aligned 2×2 comparison videos**, using reduced-order policy `no87uwhe`. Built-in asset tracking keeps the camera near the robot; flat and tilting terrain use a closer, lower view. Downhill uses a centerline view to avoid the retaining walls. Previous campaigns are preserved separately.

[Validation results](data/four_policy_20261022_v3/validation.json) · [Camera frame review](data/four_policy_20261022_v3/camera_review.json) · [Wall visibility check](data/four_policy_20261022_v3/wall_visibility.json)
