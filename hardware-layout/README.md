# 🛰️ Hardware Layout & 3D Structure

This directory contains the physical design, mass budget, and thermal management strategies for the TerraSense 3U CubeSat.

## 📏 3U Form Factor Design
The satellite follows the standard 10x10x34 cm CubeSat specification.

### 🧩 Subsystem Stack
1.  **Unit 1 (Bottom):** EPS (Electric Power System), Lithium-Ion Battery Pack, ADCS Reaction Wheels.
2.  **Unit 2 (Center):** On-Board Computer (OBC), S-Band Transceiver, Communication Interface Board.
3.  **Unit 3 (Top/Nadir):** High-Resolution Optical Camera, Sensors, GNSS Antenna.

## 🌡️ Thermal Management
- **Passive Cooling:** Surface coatings and MLI (Multi-Layer Insulation).
- **Active Monitoring:** Thermistors on battery packs and OBC.

## 🛠️ CAD Files (Planned)
- `terrasense_v1_assembly.step`
- `structure_exploded_view.pdf`
