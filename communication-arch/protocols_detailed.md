# 🖇️ TerraSense: Detailed Protocols

## 1. CAN-Bus (LSS - Local System Services)
Internal health monitoring and simple commands.

| Msg ID (Hex) | Subsystem | Function | Data Type |
| :--- | :--- | :--- | :--- |
| 0x100 | EPS | Voltage/Current Status | Float32 x 4 |
| 0x110 | ADCS | Orientation (Quaternions)| Float32 x 4 |
| 0x120 | OBC | Heartbeat / Watchdog | UInt32 |
| 0x200 | GROUND | Tele-command Receipt | UInt8 |

## 2. SpaceWire (Mission Data)
High-speed data for payload image transfer.

- **Standard:** ECSS-E-ST-50-12C.
- **Packet Structure:**
    - [Header] Target Link Address.
    - [Protocol ID] 0x01 (Image Frame).
    - [Payload] Raw CMOS Data (Compressed).
    - [EOP] End of Packet.

## 3. SPI Hookup (Flash Storage)
- **Clock:** 40 MHz.
- **Mode:** 0 (CPOL=0, CPHA=0).
- **Latency:** < 5ms for block write (512 bytes).
