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

[Full report](data/four_policy_20261022/report.md) · [Raw measurement table](data/four_policy_20261022/summary.csv)

Each task's report includes individual and 1×4 videos, PNG/PDF figures, and measurement definitions.
Early task terminations and solver failures remain visible. This is one episode per condition at seed 42.

Completed: **72 primary conditions + 3 allocation diagnostics**, with **75 individual videos**, **18 comparison videos**, and **18 PNG/PDF figure pairs**.

[Artifact validation](data/four_policy_20261022/validation.json) found no data or video issues.
