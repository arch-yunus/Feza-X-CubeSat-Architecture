# 📑 TerraSense: Advanced Software Stack

The software architecture is based on the NASA Core Flight System (cFS) for high modularity and fault tolerance.

## 1. Layers of the Software Stack
1.  **OSAL (Operating System Abstraction Layer):** Supports RTOS (FreeRTOS / RTEMS).
2.  **cFE (Core Flight Executive):** Manages message passing (Software Bus), events, and tables.
3.  **Mission Apps:**
    - `HS`: Health and Safety monitoring.
    - `CI/TO`: Command Ingest / Telemetry Output.
    - `PL`: Payload management (Image capture).
    - `AI`: Edge AI inference application.

## 2. Software Bus Topology
- **Message Passing:** Publish/Subscribe model for internode communication.
- **Execution Rate:** 10Hz for telemetry, 1Hz for health checks.

## 3. Fault Management
- **Autonomous Recovery:** Multi-level recovery actions (Reset App -> Reset Processor -> Power Cycle).
- **Safe Mode:** Minimalist state with only critical CI/TO active.
