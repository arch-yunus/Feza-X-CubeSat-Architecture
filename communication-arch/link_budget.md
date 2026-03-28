# 📡 TerraSense: Detailed RF Link Budget

## 1. UHF/VHF Link (TT&C)
Used for critical telemetry and command.

| Parameter | Unit | Value |
| :--- | :--- | :--- |
| Frequency | MHz | 437.5 |
| Transmitter Power | dBm | 30 (1W) |
| Tx Antenna Gain | dBi | 2.1 (Monopole) |
| Path Loss (500km) | dB | -139.2 |
| Rx Antenna Gain | dBi | 10 (Ground Station) |
| **Link Margin** | **dB** | **>6.0** |

## 2. S-Band Link (Payload Data)
Used for high-speed image downlink.

| Parameter | Unit | Value |
| :--- | :--- | :--- |
| Frequency | GHz | 2.45 |
| Modulation | - | QPSK |
| Data Rate | Mbps | 2.0 |
| Transmitter Power | dBm | 33 (2W) |
| Tx Antenna Gain | dBi | 6.0 (Patch) |
| Path Loss (500km) | dB | -154.5 |
| RX G/T | dB/K | 12.0 (High Gain Dish) |
| **Link Margin** | **dB** | **3.8** |

## 📐 Assumptions
- Orbital Altitude: 500 km (LEO).
- Minimum Elevation: 10 degrees.
- Atmospheric Loss: 0.5 dB.
