# Descending

Task: `IsaacContrib-Velocity-Sand-Descending-G1-29dof-MPM-Play`

One episode per policy/material, seed 42. Early terminations remain included.

| Material | Policy | Outcome | Duration (s) | Sand window (s) | vx RMSE (m/s) | vy RMSE (m/s) | wz RMSE (rad/s) |
|---|---|---|---:|---:|---:|---:|---:|
| Stiff cohesive | Reduced order (no87uwhe) | crossed sand bed | 7.400 | 4.920 | 0.373 | 0.513 | 1.111 |
| Stiff cohesive | MPM flat finetune | Stopped: bad_orientation | 4.620 | 2.000 | 0.900 | 0.460 | 2.789 |
| Stiff cohesive | MPM rough finetune | crossed sand bed | 5.460 | 2.840 | 1.254 | 0.433 | 2.342 |
| Stiff cohesive | MPM scratch | Stopped: outside_workspace | 4.300 | 1.900 | 0.710 | 0.484 | 1.856 |
| Mild sand | Reduced order (no87uwhe) | Stopped: bad_orientation | 4.840 | 2.420 | 1.132 | 0.393 | 1.941 |
| Mild sand | MPM flat finetune | crossed sand bed | 5.960 | 3.300 | 0.617 | 0.166 | 1.241 |
| Mild sand | MPM rough finetune | Stopped: outside_workspace | 6.440 | 4.000 | 0.331 | 0.154 | 1.003 |

![Tracking](tracking.png)

[Tracking PDF](tracking.pdf)

| Material | Policy | Steps / swings | Step duration (s) | Signed X step length (m) | Clearance (cm) | Swing lift (cm) |
|---|---|---:|---:|---:|---:|---:|
| Stiff cohesive | Reduced order (no87uwhe) | 15 / 18 | 0.227 ± 0.095 | 0.237 ± 0.291 | 8.613 ± 5.102 | 8.196 ± 5.040 |
| Stiff cohesive | MPM flat finetune | 5 / 5 | 0.208 ± 0.155 | 0.348 ± 0.584 | 24.152 ± 13.852 | 22.718 ± 13.349 |
| Stiff cohesive | MPM rough finetune | 9 / 8 | 0.233 ± 0.079 | 0.415 ± 0.139 | 23.995 ± 6.138 | 23.825 ± 6.346 |
| Stiff cohesive | MPM scratch | 3 / 4 | 0.227 ± 0.041 | 0.631 ± 0.056 | 21.223 ± 11.183 | 21.100 ± 10.291 |
| Mild sand | Reduced order (no87uwhe) | 3 / 3 | 0.540 ± 0.400 | 0.985 ± 0.865 | 7.510 ± 6.061 | 0.747 ± 0.549 |
| Mild sand | MPM flat finetune | 9 / 11 | 0.173 ± 0.128 | 0.238 ± 0.417 | 1.831 ± 5.494 | 5.802 ± 4.596 |
| Mild sand | MPM rough finetune | 9 / 10 | 0.307 ± 0.205 | 0.255 ± 0.201 | -1.286 ± 2.883 | 4.554 ± 2.990 |

![Gait](gait.png)

[Gait PDF](gait.pdf)

![Traces](traces.png)

[Traces PDF](traces.pdf)

Gait bars show variation between events in one rollout, not uncertainty across seeds. Clearance uses the initial surface, not the deformed particle surface. Signed X steps can be negative during backward motion and do not measure lateral step length. Missing points mean no complete eligible event.

## Videos

- [basalt_like: 2×2 comparison](../../../videos/four_policy_20261022_v2/descending/comparison_basalt_like.mp4)
  - [Reduced order (no87uwhe)](../../../videos/four_policy_20261022_v2/descending/basalt_like__soft_contact__seed42/rollout.mp4) · [raw data](basalt_like__soft_contact__seed42/trace.npz) · [events](basalt_like__soft_contact__seed42/gait_events.json)
  - [MPM flat finetune](../../../videos/four_policy_20261022_v2/descending/basalt_like__mpm_flat__seed42/rollout.mp4) · [raw data](basalt_like__mpm_flat__seed42/trace.npz) · [events](basalt_like__mpm_flat__seed42/gait_events.json)
  - [MPM rough finetune](../../../videos/four_policy_20261022_v2/descending/basalt_like__mpm_rough__seed42/rollout.mp4) · [raw data](basalt_like__mpm_rough__seed42/trace.npz) · [events](basalt_like__mpm_rough__seed42/gait_events.json)
  - [MPM scratch](../../../videos/four_policy_20261022_v2/descending/basalt_like__scratch__seed42/rollout.mp4) · [raw data](basalt_like__scratch__seed42/trace.npz) · [events](basalt_like__scratch__seed42/gait_events.json)
- [mild_sand: 2×2 comparison](../../../videos/four_policy_20261022_v2/descending/comparison_mild_sand.mp4)
  - [Reduced order (no87uwhe)](../../../videos/four_policy_20261022_v2/descending/mild_sand__soft_contact__seed42/rollout.mp4) · [raw data](mild_sand__soft_contact__seed42/trace.npz) · [events](mild_sand__soft_contact__seed42/gait_events.json)
  - [MPM flat finetune](../../../videos/four_policy_20261022_v2/descending/mild_sand__mpm_flat__seed42/rollout.mp4) · [raw data](mild_sand__mpm_flat__seed42/trace.npz) · [events](mild_sand__mpm_flat__seed42/gait_events.json)
  - [MPM rough finetune](../../../videos/four_policy_20261022_v2/descending/mild_sand__mpm_rough__seed42/rollout.mp4) · [raw data](mild_sand__mpm_rough__seed42/trace.npz) · [events](mild_sand__mpm_rough__seed42/gait_events.json)
  - [MPM scratch](../../../videos/four_policy_20261022_v2/descending/mild_sand__scratch__seed42/rollout.mp4) · [raw data](mild_sand__scratch__seed42/trace.npz) · [events](mild_sand__scratch__seed42/gait_events.json)
- [soft_sand: 2×2 comparison](../../../videos/four_policy_20261022_v2/descending/comparison_soft_sand.mp4)
  - [Reduced order (no87uwhe)](../../../videos/four_policy_20261022_v2/descending/soft_sand__soft_contact__seed42/rollout.mp4) · [raw data](soft_sand__soft_contact__seed42/trace.npz) · [events](soft_sand__soft_contact__seed42/gait_events.json)
  - [MPM flat finetune](../../../videos/four_policy_20261022_v2/descending/soft_sand__mpm_flat__seed42/rollout.mp4) · [raw data](soft_sand__mpm_flat__seed42/trace.npz) · [events](soft_sand__mpm_flat__seed42/gait_events.json)
  - [MPM rough finetune](../../../videos/four_policy_20261022_v2/descending/soft_sand__mpm_rough__seed42/rollout.mp4) · [raw data](soft_sand__mpm_rough__seed42/trace.npz) · [events](soft_sand__mpm_rough__seed42/gait_events.json)
  - [MPM scratch](../../../videos/four_policy_20261022_v2/descending/soft_sand__scratch__seed42/rollout.mp4) · [raw data](soft_sand__scratch__seed42/trace.npz) · [events](soft_sand__scratch__seed42/gait_events.json)
