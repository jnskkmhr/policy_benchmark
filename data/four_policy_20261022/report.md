# Four-policy MPM benchmark — 22 October 2026

**Recorded 61 of 72 conditions:** four policies × three materials × six Play tasks.

## Results

A completed crossing reaches the far side of the sand bed. A completed tilting trial lasts 30 seconds without a task termination. The table counts those completions out of three materials; solver errors are not policy failures.

| Task | Reduced order | MPM flat finetune | MPM rough finetune | MPM scratch |
|---|---:|---:|---:|---:|
| [flat](flat/report.md) | 1/3 | 3/3 | 3/3 | 3/3 |
| [ascending](ascending/report.md) | 0/3 | 1/3 | 0/3 | 1/3 |
| [descending](descending/report.md) | 0/3 | 0/3 | 1/3 | 1/3 |
| [dune](dune/report.md) | 1/3 | 3/3 | 2/3 | 2/3 |
| [standing tilt](standing_tilt/report.md) | 0/1 recorded | 0/1 recorded | 1/1 recorded | 0/0 recorded |
| [walking tilt](walking_tilt/report.md) | 1/3 | 3/3 | 2/2 recorded | 2/2 recorded |

**Failures and stops:**

- **Reduced order:** flat/mild_sand: Stopped: outside_workspace at 5.08 s; flat/soft_sand: Stopped: bad_orientation at 3.44 s; ascending/basalt_like: Stopped: bad_orientation at 3.08 s; ascending/mild_sand: Stopped: base_too_low at 3.18 s; ascending/soft_sand: Stopped: bad_orientation at 2.82 s; descending/basalt_like: Stopped: bad_orientation at 4.00 s; descending/mild_sand: Stopped: bad_orientation at 3.94 s; descending/soft_sand: Stopped: bad_orientation at 4.54 s; dune/mild_sand: Stopped: bad_orientation at 3.28 s; dune/soft_sand: Stopped: bad_orientation at 3.12 s; standing_tilt/basalt_like: Stopped: outside_workspace at 8.96 s; walking_tilt/mild_sand: Stopped: outside_workspace at 2.96 s; walking_tilt/soft_sand: Stopped: bad_orientation at 2.24 s
- **MPM flat finetune:** ascending/basalt_like: Stopped: outside_workspace at 12.84 s; ascending/soft_sand: solver capacity error at 4.58 s; descending/basalt_like: Stopped: bad_orientation at 4.18 s; descending/mild_sand: Stopped: bad_orientation at 5.22 s; descending/soft_sand: Stopped: bad_orientation at 4.90 s; standing_tilt/basalt_like: Stopped: outside_workspace at 24.10 s
- **MPM rough finetune:** ascending/basalt_like: time limit at 13.00 s; ascending/mild_sand: Stopped: outside_workspace at 7.00 s; ascending/soft_sand: solver capacity error at 4.60 s; descending/basalt_like: Stopped: extreme_action at 4.52 s; descending/soft_sand: Stopped: bad_orientation at 3.30 s; dune/basalt_like: Stopped: outside_workspace at 9.78 s
- **MPM scratch:** ascending/basalt_like: Stopped: outside_workspace at 10.04 s; ascending/soft_sand: solver capacity error at 4.58 s; descending/basalt_like: Stopped: bad_orientation at 3.58 s; descending/soft_sand: Stopped: bad_orientation at 4.70 s; dune/basalt_like: Stopped: outside_workspace at 8.70 s

Per-task reports above contain every RMSE, step measurement, individual video, and 1×4 comparison.
[All measurements: CSV](summary.csv) · [JSON](summary.json)

## Policies

| Policy | Run | Checkpoint |
|---|---|---|
| Reduced order | [tyiby5k6](https://forge.coreweave.com/wandb/jnskkmr/g1_29dof_soft_flat_ppo/runs/tyiby5k6) | `model_19999.pt` |
| MPM flat finetune | [evh180n4](https://forge.coreweave.com/wandb/jnskkmr/g1_29dof_mpm_mixed_terrain/runs/evh180n4) | `model_39998.pt` |
| MPM rough finetune | [5f1xyc21](https://forge.coreweave.com/wandb/jnskkmr/g1_29dof_mpm_mixed_terrain/runs/5f1xyc21) | `model_39998.pt` |
| MPM scratch | [876gqr97](https://forge.coreweave.com/wandb/jnskkmr/g1_29dof_mpm_mixed_terrain/runs/876gqr97) | `model_19999.pt` |

Latest available checkpoint per requested run, frozen by SHA-256 in [checkpoints.json](checkpoints.json). All actors load strictly with 937 inputs and 29 actions. Actors use 10-frame term-wise history plus the command group. Critics are unused. Observation corruption is disabled.

## Material presets

| Material | Density (kg/m³) | Young's modulus (Pa) | Friction | Yield pressure (Pa) | Yield stress (Pa) | Tensile yield ratio |
|---|---:|---:|---:|---:|---:|---:|
| Stiff cohesive | 2700 | 4e+10 | 0.8391 | 1e+09 | 1e+08 | 1 |
| Mild sand | 1600 | 1e+15 | 0.48 | 1e+15 | 0 | 0 |
| Soft sand | 1000 | 1e+06 | 0.3 | 1e+15 | 0 | 0 |

These reproduce the earlier benchmark presets. Stiff cohesive is the requested almost-solid proxy, not calibrated basalt or rigid collision. Mild sand has a higher elastic modulus but no cohesion; the names do not rank Young's modulus. Several parameters change together. [All material parameters](materials.json).

## Protocol and measurements

Stationary beds are 6 × 2 m with a 0.3 m initial particle layer. Ascending/descending ramps have slope ±0.4 (±21.8 degrees); the dune has two ridges of height 0.3 m. The standing tray is 3 × 2 m and the walking tray is 4 × 4 m, both with a 0.3 m particle layer. Standing-tray roll/pitch amplitudes are ±15 degrees; walking-tray amplitudes are ±10 degrees. Both use 12 s roll and 17 s pitch periods, 2 s settling, and a 3 s ramp. MPM voxel size is 0.04 m, policy timestep 0.02 s, and physics timestep 0.005 s.

- One episode per condition with deterministic actor outputs, seed 42, using current Play scenes. No task implementation was changed for this benchmark. Each rollout saves its resolved configuration and log.
- Flat, ascending, descending, and dune: forward command 1 m/s, lateral and yaw-rate commands zero; start on the approach platform. Stop at the first termination, 13 s, or base X 0.4 m before the far bed edge.
- Standing tilt: zero command for 30 s. Walking tilt: 4 s each of forward/backward ±0.25 m/s, left/right ±0.25 m/s, yaw ±0.3 rad/s, then zero command to 30 s. Tray motion is the current task's configured motion, identical between policies for the same task.
- Tracking window: both ankle links inside the sand bed with 0.15 m edge margin, after 0.5 s. Linear velocity uses the gravity-aligned robot heading frame; yaw rate uses world Z. Traces show the whole episode; RMSE uses only the sand window.
- Contact transitions must persist for 60 ms. Step duration is the interval between consecutive opposite-foot touchdowns. Step length is signed ankle-link displacement along X, in world coordinates for stationary beds and tray coordinates for tilting beds.
- Clearance is peak height of the lowest collision-sole corner relative to the initial sand surface at that XY, or the initial surface in tray coordinates. It is not clearance above the moving particle surface. Swing lift subtracts sole height at liftoff. Only complete steps/swings inside the sand window count.
- Videos are RTX, 960×540 per policy, 25 FPS. Tiled videos place all four policies in one row at matching episode times. Finished rollouts hold the final frame with a label.

## Limits

This is a single-seed comparison, not a statistical ranking. Newton does not guarantee bitwise deterministic replay. Gait error bars are event standard deviations within one rollout. Failed policies have shorter measurement windows, so low RMSE alone is not success. Zero eligible gait events are shown as missing, not zero. A workspace termination is reported as such, rather than automatically called a fall. Backward and lateral walking make signed X step length insufficient as a general stride-distance measure. No inference about real sand or hardware is made.

## Reproduce

Run from the repository root with the existing environment:

```bash
uv run --no-sync --with wandb python source/isaaclab_tasks/isaaclab_tasks/contrib/g1_29dof_mpm/benchmark_2/run_comparison.py --all
uv run --no-sync python source/isaaclab_tasks/isaaclab_tasks/contrib/g1_29dof_mpm/benchmark_2/analyze_comparison.py --videos
```

The runner resumes by skipping completed conditions. To rerun a condition, use a fresh campaign directory. `--prepare` resolves the latest W&B checkpoint again; the supplied manifest is the frozen record for these results.
[Dependency versions and source hashes](provenance.json).

## Grid-capacity diagnostics

These additional trials increase leaf-node allocation from 8,192 to 32,768; physical parameters and commands are unchanged. They do not replace the original 72-condition table.

| Task | Policy | Material | Retry outcome | Duration (s) | Data / video |
|---|---|---|---|---:|---|
| ascending | mpm_flat | soft_sand | terminated: outside_workspace | 9.34 | [Metadata](capacity_retries/ascending/soft_sand__mpm_flat__seed42/metadata.json) · [Video](../../videos/four_policy_20261022/capacity_retries/ascending/soft_sand__mpm_flat__seed42/rollout.mp4) |
| ascending | mpm_rough | soft_sand | terminated: outside_workspace | 9.46 | [Metadata](capacity_retries/ascending/soft_sand__mpm_rough__seed42/metadata.json) · [Video](../../videos/four_policy_20261022/capacity_retries/ascending/soft_sand__mpm_rough__seed42/rollout.mp4) |
| ascending | scratch | soft_sand | terminated: outside_workspace | 12.70 | [Metadata](capacity_retries/ascending/soft_sand__scratch__seed42/metadata.json) · [Video](../../videos/four_policy_20261022/capacity_retries/ascending/soft_sand__scratch__seed42/rollout.mp4) |