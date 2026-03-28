# 📡 Communication & Data Architecture

This directory outlines the internal data bus and external RF links for the TerraSense mission.

## 🖇️ Internal Bus Topology
- **CAN Bus (System Control):** Used for EPS, ADCS, and OBC telemetry. High fault tolerance and simplified wiring.
- **SpaceWire / LVDS (Mission Data):** Dedicated high-speed link between the Payload (Camera) and Mass Storage.

## 🌍 External Communication (Link Budget)
| Feature | Link 1: TT&C | Link 2: Payload Downlink |
| :--- | :--- | :--- |
| **Band** | UHF / VHF | S-Band |
| **Data Rate** | 9.6 kbps | Up to 2 Mbps |
| **Antenna** | Monopole (Omni) | Patch Antenna (High Gain) |
| **Protocol** | AX.25 | CCSDS |

## 📐 Network Diagrams
- `internal_bus_wiring.png`
- `rf_link_budget_calc.xlsx`
