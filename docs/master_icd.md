# 📟 Master Interface Control Document (ICD) v1.1

This document defines the physical, electrical, and logical interfaces for the Feza-X 3U CubeSat platform.

## 1. Physical Interface (PC104 Bus)
Feza-X uses the standard PC104 stacking connector for inter-subsystem power and data.

| Pin Number | Signal Name | Voltage | Description |
| :--- | :--- | :--- | :--- |
| **H1, H2** | 5V Bus | 5.0V | Main digital power rail (Regulated) |
| **H3, H4** | 3.3V Bus | 3.3V | Low-power digital rail (OBC/Sensors) |
| **H5, H6** | 12V Bus | 12.0V | Unregulated Battery Rail (Actuators/Comms) |
| **H7, H8** | GND | 0.0V | Common system ground |
| **H9** | CAN-H | 2.5V - 3.5V | High-speed Control Bus (Critical) |
| **H10** | CAN-L | 1.5V - 2.5V | High-speed Control Bus (Critical) |
| **H11, H12** | I2C-SDA, SCL | 3.3V | Sensor Bus (Non-critical) |

## 2. Logical Interface (CSP Ports)
Subsystem communication is handled via **CubeSat Space Protocol (CSP)** over the CAN-Bus.

| Port | Service Name | Protocol | Description |
| :--- | :--- | :--- | :--- |
| **1** | Ping Service | ICMP-like | Connectivity check for all nodes. |
| **7** | PDU Service | Binary | Power Distribution Unit Telemetry. |
| **10** | Command Rx | HMAC-Signed | Uplink ground command ingestion. |
| **31** | Payload Data | SpaceWire/SPI | Raw science data transfer. |
| **40** | FDIR Log | Text | Fault detection and event logging. |

## 3. Connector Specifications
- **Type:** Samtec ESQ series (2x26 pins).
- **Pitch:** 2.54 mm.
- **Housing:** Gold-plated contacts for space vacuum environment.

## 4. Ground Support Interface (UMBILICAL)
- **External Port:** 15-pin D-SUB (MALE) on the satellite frame.
- **Function:** Battery charging, Serial Debug (UART), and Remove-Before-Flight (RBF) pin.
