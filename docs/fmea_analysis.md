# ⚠️ TerraSense: Failure Mode & Effects Analysis (FMEA)

This document analyzes potential system failures and defines mitigation strategies for the TerraSense mission.

## 1. Subsystem Failure Matrix

| Component | Failure Mode | Impact | Mitigation Strategy |
| :--- | :--- | :--- | :--- |
| **EPS** | Battery Overheating | System Shutdown | Autonomous thermal cutout & heater active control. |
| **OBC** | Single Event Upset (SEU) | Data Corruption | ECC RAM + Watchdog timer for auto-reboot. |
| **ADCS** | Reaction Wheel Saturation | Loss of Pointing | De-saturation using Magnetorquers (Magnetic Torquing). |
| **Comms** | S-Band Link Failure | No Payload Data | Fallback to UHF for low-res "thumbnail" data transfer. |
| **Payload** | Lens Fogging/Outgassing | Image Blur | Pre-launch bake-out & integrated lens heaters. |

## 2. Redundancy Scheme
- **Command & Control:** Dual UHF monopole antennas to ensure reception regardless of orientation.
- **Data Storage:** RAID-1 mirrored NAND flash for critical mission telemetry.
- **Power:** Multi-junction solar cells arranged in independent strings (parallel strings) to avoid total power loss if one string is damaged.
