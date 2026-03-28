# 🧩 TerraSense: Subsystem Specifications (SWaP-C)

Detailed specifications for the 3U CubeSat modules.

## 🔋 EPS (Electric Power System) - Unit 1
- **Model:** Generic High-Efficiency 3U EPS.
- **Solar Panels:** 7x Triple-junction Gallium Arsenide (GaAs) cells per 3U face.
- **Batteries:** 40Wh Li-Ion (4S1P configuration) with built-in heater.
- **Output:** 3.3V, 5V, and 12V regulated rails.
- **Efficiency:** >92% (MPPT regulated).

## 🧭 ADCS (Attitude Determination and Control System) - Unit 1
- **Sensors:** 6x Sun sensors, 3-axis Magnetometer, 3-axis MEMS Gyro.
- **Actuators:** 3x Reaction Wheels (0.1 mNms), 3x Magnetorquers.
- **Pointing Accuracy:** <0.5 degrees.
- **Stability:** 0.1 deg/s.

## 🧠 OBC (On-Board Computer) - Unit 2
- **Processor:** Dual-core ARM Cortex-A5 (Rad-Hardened by Design).
- **RAM:** 512MB ECC DDR3.
- **Storage:** 32GB Industrial Grade NAND Flash (Mass Storage).
- **Interface:** CAN, I2C, SPI, UART, SpaceWire.

## 📸 Payload (Optical Sensor) - Unit 3
- **Sensor:** CMOS RGB/NIR Sensor.
- **Resolution:** 5.0m GSD at 500km orbit.
- **Focal Length:** 500mm (folded optics).
- **Format:** 4096 x 3072 pixels.
- **Data Interface:** LVDS / SpaceWire for raw frame transfer.
