# 🛠️ TerraSense: Assembly, Integration & Test (AIT)

Procedures for physical assembly and environmental testing of the TerraSense flight model.

## 1. Assembly Sequence
1.  **Structure Preparation:** Inspect 3U frame for tolerances and clean with IPA.
2.  **Backplane Integration:** Install internal bus (PC104 headers).
3.  **Module Stacking:**
    - Insert Unit 1 (EPS/ADCS).
    - Insert Unit 2 (OBC/Comms).
    - Insert Unit 3 (Payload).
4.  **Cabling:** Connect solar panel bundles and deployable antenna triggers.

## 2. Environmental Testing Checklist
- [ ] **Vibration Test:** Random vibration (Launcher profile) to ensure structural integrity.
- [ ] **Thermal Vacuum (TVAC):** Verify subsystem operation at thermal extremes in a vacuum.
- [ ] **EMI/EMC:** Check for internal electromagnetic interference between S-Band and OBC.
- [ ] **Deployment Test:** Burn-wire trigger verification for solar panels and antennas.

## 3. Functional Testing (Day-In-The-Life)
A full 95-minute mission simulation on the ground:
- Sunlight simulation (Charging).
- Imaging mode (Payload power spike).
- Eclipse simulation (Battery discharge).
- Command uplink & Data downlink sequence.
