# Descending

Task: `IsaacContrib-Velocity-Sand-Descending-G1-29dof-MPM-Play`

One episode per policy/material, seed 42. Early terminations remain included.

| Material | Policy | Outcome | Duration (s) | Sand window (s) | vx RMSE (m/s) | vy RMSE (m/s) | wz RMSE (rad/s) |
|---|---|---|---:|---:|---:|---:|---:|
| Stiff cohesive | Reduced order (no87uwhe) | Stopped: bad_orientation | 5.540 | 3.120 | 0.414 | 0.139 | 0.582 |
| Stiff cohesive | MPM flat finetune | Stopped: bad_orientation | 4.120 | 1.500 | 1.327 | 0.239 | 2.009 |
| Stiff cohesive | MPM rough finetune | crossed sand bed | 6.840 | 4.320 | 0.746 | 0.358 | 1.710 |
| Stiff cohesive | MPM scratch | Stopped: bad_orientation | 3.520 | 1.220 | 0.798 | 0.375 | 1.680 |
| Mild sand | Reduced order (no87uwhe) | crossed sand bed | 5.120 | 2.700 | 1.213 | 0.342 | 1.976 |
| Mild sand | MPM flat finetune | crossed sand bed | 5.900 | 3.280 | 0.642 | 0.137 | 1.117 |
| Mild sand | MPM rough finetune | crossed sand bed | 7.280 | 4.840 | 0.358 | 0.137 | 0.931 |
| Mild sand | MPM scratch | Stopped: outside_workspace | 4.840 | 2.540 | 0.424 | 0.207 | 1.081 |
| Soft sand | Reduced order (no87uwhe) | Stopped: base_too_low | 4.020 | 1.600 | 1.188 | 0.600 | 2.285 |
| Soft sand | MPM flat finetune | Stopped: outside_workspace | 4.720 | 2.060 | 0.545 | 0.283 | 1.695 |
| Soft sand | MPM rough finetune | Stopped: bad_orientation | 3.340 | 0.900 | 0.474 | 0.286 | 1.528 |
| Soft sand | MPM scratch | Stopped: bad_orientation | 5.080 | 2.780 | 1.159 | 0.557 | 2.488 |

![Tracking](tracking.png)

[Tracking PDF](tracking.pdf)

| Material | Policy | Steps / swings | Step duration (s) | Signed X step length (m) | Clearance (cm) | Swing lift (cm) |
|---|---|---:|---:|---:|---:|---:|
| Stiff cohesive | Reduced order (no87uwhe) | 10 / 11 | 0.254 ± 0.070 | 0.297 ± 0.191 | 8.988 ± 3.167 | 9.232 ± 2.936 |
| Stiff cohesive | MPM flat finetune | 3 / 3 | 0.287 ± 0.180 | 0.744 ± 0.459 | 16.633 ± 10.228 | 15.777 ± 11.060 |
| Stiff cohesive | MPM rough finetune | 13 / 14 | 0.220 ± 0.063 | 0.293 ± 0.121 | 19.347 ± 3.720 | 18.473 ± 3.578 |
| Stiff cohesive | MPM scratch | 1 / 1 | 0.260 ± 0.000 | 0.491 ± 0.000 | 38.144 ± 0.000 | 38.512 ± 0.000 |
| Mild sand | Reduced order (no87uwhe) | 2 / 3 | 0.520 ± 0.480 | 1.072 ± 1.015 | 18.958 ± 12.493 | 4.015 ± 5.679 |
| Mild sand | MPM flat finetune | 11 / 12 | 0.218 ± 0.159 | 0.348 ± 0.511 | 0.095 ± 5.173 | 5.752 ± 4.173 |
| Mild sand | MPM rough finetune | 11 / 10 | 0.384 ± 0.234 | 0.407 ± 0.236 | 0.020 ± 1.988 | 6.463 ± 4.674 |
| Mild sand | MPM scratch | 5 / 5 | 0.320 ± 0.226 | 0.453 ± 0.079 | 4.063 ± 2.962 | 10.524 ± 7.266 |
| Soft sand | Reduced order (no87uwhe) | 3 / 3 | 0.247 ± 0.223 | 0.350 ± 0.719 | 1.916 ± 6.695 | 23.381 ± 11.912 |
| Soft sand | MPM flat finetune | 4 / 5 | 0.220 ± 0.130 | 0.365 ± 0.046 | -17.856 ± 5.515 | 9.612 ± 5.505 |
| Soft sand | MPM rough finetune | 0 / 1 | — | — | -21.780 ± 0.000 | 6.039 ± 0.000 |
| Soft sand | MPM scratch | 6 / 6 | 0.363 ± 0.208 | 0.570 ± 0.505 | 10.259 ± 30.354 | 36.586 ± 29.717 |

![Gait](gait.png)

[Gait PDF](gait.pdf)

![Traces](traces.png)

[Traces PDF](traces.pdf)

Gait bars show variation between events in one rollout, not uncertainty across seeds. Clearance uses the initial surface, not the deformed particle surface. Signed X steps can be negative during backward motion and do not measure lateral step length. Missing points mean no complete eligible event.

## Videos

- [basalt_like: 2×2 comparison](../../../videos/four_policy_20261022_v3/descending/comparison_basalt_like.mp4)
  - [Reduced order (no87uwhe)](../../../videos/four_policy_20261022_v3/descending/basalt_like__soft_contact__seed42/rollout.mp4) · [raw data](basalt_like__soft_contact__seed42/trace.npz) · [events](basalt_like__soft_contact__seed42/gait_events.json)
  - [MPM flat finetune](../../../videos/four_policy_20261022_v3/descending/basalt_like__mpm_flat__seed42/rollout.mp4) · [raw data](basalt_like__mpm_flat__seed42/trace.npz) · [events](basalt_like__mpm_flat__seed42/gait_events.json)
  - [MPM rough finetune](../../../videos/four_policy_20261022_v3/descending/basalt_like__mpm_rough__seed42/rollout.mp4) · [raw data](basalt_like__mpm_rough__seed42/trace.npz) · [events](basalt_like__mpm_rough__seed42/gait_events.json)
  - [MPM scratch](../../../videos/four_policy_20261022_v3/descending/basalt_like__scratch__seed42/rollout.mp4) · [raw data](basalt_like__scratch__seed42/trace.npz) · [events](basalt_like__scratch__seed42/gait_events.json)
- [mild_sand: 2×2 comparison](../../../videos/four_policy_20261022_v3/descending/comparison_mild_sand.mp4)
  - [Reduced order (no87uwhe)](../../../videos/four_policy_20261022_v3/descending/mild_sand__soft_contact__seed42/rollout.mp4) · [raw data](mild_sand__soft_contact__seed42/trace.npz) · [events](mild_sand__soft_contact__seed42/gait_events.json)
  - [MPM flat finetune](../../../videos/four_policy_20261022_v3/descending/mild_sand__mpm_flat__seed42/rollout.mp4) · [raw data](mild_sand__mpm_flat__seed42/trace.npz) · [events](mild_sand__mpm_flat__seed42/gait_events.json)
  - [MPM rough finetune](../../../videos/four_policy_20261022_v3/descending/mild_sand__mpm_rough__seed42/rollout.mp4) · [raw data](mild_sand__mpm_rough__seed42/trace.npz) · [events](mild_sand__mpm_rough__seed42/gait_events.json)
  - [MPM scratch](../../../videos/four_policy_20261022_v3/descending/mild_sand__scratch__seed42/rollout.mp4) · [raw data](mild_sand__scratch__seed42/trace.npz) · [events](mild_sand__scratch__seed42/gait_events.json)
- [soft_sand: 2×2 comparison](../../../videos/four_policy_20261022_v3/descending/comparison_soft_sand.mp4)
  - [Reduced order (no87uwhe)](../../../videos/four_policy_20261022_v3/descending/soft_sand__soft_contact__seed42/rollout.mp4) · [raw data](soft_sand__soft_contact__seed42/trace.npz) · [events](soft_sand__soft_contact__seed42/gait_events.json)
  - [MPM flat finetune](../../../videos/four_policy_20261022_v3/descending/soft_sand__mpm_flat__seed42/rollout.mp4) · [raw data](soft_sand__mpm_flat__seed42/trace.npz) · [events](soft_sand__mpm_flat__seed42/gait_events.json)
  - [MPM rough finetune](../../../videos/four_policy_20261022_v3/descending/soft_sand__mpm_rough__seed42/rollout.mp4) · [raw data](soft_sand__mpm_rough__seed42/trace.npz) · [events](soft_sand__mpm_rough__seed42/gait_events.json)
  - [MPM scratch](../../../videos/four_policy_20261022_v3/descending/soft_sand__scratch__seed42/rollout.mp4) · [raw data](soft_sand__scratch__seed42/trace.npz) · [events](soft_sand__scratch__seed42/gait_events.json)
