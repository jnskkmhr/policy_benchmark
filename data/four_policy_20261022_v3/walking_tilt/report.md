# Walking Tilt

Task: `IsaacContrib-Velocity-Sand-Tilting-G1-29dof-MPM-Play`

One episode per policy/material, seed 42. Early terminations remain included.

| Material | Policy | Outcome | Duration (s) | Sand window (s) | vx RMSE (m/s) | vy RMSE (m/s) | wz RMSE (rad/s) |
|---|---|---|---:|---:|---:|---:|---:|
| Stiff cohesive | Reduced order (no87uwhe) | Stopped: bad_orientation | 6.080 | 5.580 | 0.323 | 0.202 | 0.401 |
| Stiff cohesive | MPM flat finetune | time limit | 30.000 | 29.500 | 0.131 | 0.109 | 0.416 |
| Mild sand | Reduced order (no87uwhe) | Stopped: outside_workspace | 2.660 | 2.160 | 0.860 | 0.105 | 1.071 |
| Mild sand | MPM flat finetune | time limit | 30.000 | 29.500 | 0.096 | 0.073 | 0.257 |
| Mild sand | MPM scratch | time limit | 30.000 | 29.500 | 0.077 | 0.064 | 0.267 |
| Soft sand | Reduced order (no87uwhe) | Stopped: outside_workspace | 2.460 | 1.960 | 0.845 | 0.080 | 1.075 |
| Soft sand | MPM flat finetune | time limit | 30.000 | 29.500 | 0.128 | 0.102 | 0.312 |

![Tracking](tracking.png)

[Tracking PDF](tracking.pdf)

| Material | Policy | Steps / swings | Step duration (s) | Signed X step length (m) | Clearance (cm) | Swing lift (cm) |
|---|---|---:|---:|---:|---:|---:|
| Stiff cohesive | Reduced order (no87uwhe) | 8 / 10 | 0.242 ± 0.114 | 0.078 ± 0.178 | 8.162 ± 3.056 | 6.781 ± 3.073 |
| Stiff cohesive | MPM flat finetune | 79 / 81 | 0.319 ± 0.306 | -0.007 ± 0.122 | 8.861 ± 4.807 | 7.663 ± 4.769 |
| Mild sand | Reduced order (no87uwhe) | 1 / 2 | 0.200 ± 0.000 | 0.523 ± 0.000 | 5.923 ± 1.429 | 2.064 ± 2.064 |
| Mild sand | MPM flat finetune | 54 / 58 | 0.320 ± 0.095 | 0.018 ± 0.098 | -7.128 ± 4.433 | 6.445 ± 3.624 |
| Mild sand | MPM scratch | 68 / 69 | 0.430 ± 0.073 | 0.006 ± 0.118 | -3.138 ± 3.300 | 12.062 ± 3.978 |
| Soft sand | Reduced order (no87uwhe) | 0 / 0 | — | — | — | — |
| Soft sand | MPM flat finetune | 22 / 30 | 0.597 ± 1.307 | 0.027 ± 0.102 | -12.358 ± 3.218 | 6.380 ± 3.535 |

![Gait](gait.png)

[Gait PDF](gait.pdf)

![Traces](traces.png)

[Traces PDF](traces.pdf)

Gait bars show variation between events in one rollout, not uncertainty across seeds. Clearance uses the initial surface, not the deformed particle surface. Signed X steps can be negative during backward motion and do not measure lateral step length. Missing points mean no complete eligible event.

## Videos

- [basalt_like: 2×2 comparison](../../../videos/four_policy_20261022_v3/walking_tilt/comparison_basalt_like.mp4)
  - [Reduced order (no87uwhe)](../../../videos/four_policy_20261022_v3/walking_tilt/basalt_like__soft_contact__seed42/rollout.mp4) · [raw data](basalt_like__soft_contact__seed42/trace.npz) · [events](basalt_like__soft_contact__seed42/gait_events.json)
  - [MPM flat finetune](../../../videos/four_policy_20261022_v3/walking_tilt/basalt_like__mpm_flat__seed42/rollout.mp4) · [raw data](basalt_like__mpm_flat__seed42/trace.npz) · [events](basalt_like__mpm_flat__seed42/gait_events.json)
  - [MPM rough finetune](../../../videos/four_policy_20261022_v3/walking_tilt/basalt_like__mpm_rough__seed42/rollout.mp4) · [raw data](basalt_like__mpm_rough__seed42/trace.npz) · [events](basalt_like__mpm_rough__seed42/gait_events.json)
  - [MPM scratch](../../../videos/four_policy_20261022_v3/walking_tilt/basalt_like__scratch__seed42/rollout.mp4) · [raw data](basalt_like__scratch__seed42/trace.npz) · [events](basalt_like__scratch__seed42/gait_events.json)
- [mild_sand: 2×2 comparison](../../../videos/four_policy_20261022_v3/walking_tilt/comparison_mild_sand.mp4)
  - [Reduced order (no87uwhe)](../../../videos/four_policy_20261022_v3/walking_tilt/mild_sand__soft_contact__seed42/rollout.mp4) · [raw data](mild_sand__soft_contact__seed42/trace.npz) · [events](mild_sand__soft_contact__seed42/gait_events.json)
  - [MPM flat finetune](../../../videos/four_policy_20261022_v3/walking_tilt/mild_sand__mpm_flat__seed42/rollout.mp4) · [raw data](mild_sand__mpm_flat__seed42/trace.npz) · [events](mild_sand__mpm_flat__seed42/gait_events.json)
  - [MPM rough finetune](../../../videos/four_policy_20261022_v3/walking_tilt/mild_sand__mpm_rough__seed42/rollout.mp4) · [raw data](mild_sand__mpm_rough__seed42/trace.npz) · [events](mild_sand__mpm_rough__seed42/gait_events.json)
  - [MPM scratch](../../../videos/four_policy_20261022_v3/walking_tilt/mild_sand__scratch__seed42/rollout.mp4) · [raw data](mild_sand__scratch__seed42/trace.npz) · [events](mild_sand__scratch__seed42/gait_events.json)
- [soft_sand: 2×2 comparison](../../../videos/four_policy_20261022_v3/walking_tilt/comparison_soft_sand.mp4)
  - [Reduced order (no87uwhe)](../../../videos/four_policy_20261022_v3/walking_tilt/soft_sand__soft_contact__seed42/rollout.mp4) · [raw data](soft_sand__soft_contact__seed42/trace.npz) · [events](soft_sand__soft_contact__seed42/gait_events.json)
  - [MPM flat finetune](../../../videos/four_policy_20261022_v3/walking_tilt/soft_sand__mpm_flat__seed42/rollout.mp4) · [raw data](soft_sand__mpm_flat__seed42/trace.npz) · [events](soft_sand__mpm_flat__seed42/gait_events.json)
  - [MPM rough finetune](../../../videos/four_policy_20261022_v3/walking_tilt/soft_sand__mpm_rough__seed42/rollout.mp4) · [raw data](soft_sand__mpm_rough__seed42/trace.npz) · [events](soft_sand__mpm_rough__seed42/gait_events.json)
  - [MPM scratch](../../../videos/four_policy_20261022_v3/walking_tilt/soft_sand__scratch__seed42/rollout.mp4) · [raw data](soft_sand__scratch__seed42/trace.npz) · [events](soft_sand__scratch__seed42/gait_events.json)
