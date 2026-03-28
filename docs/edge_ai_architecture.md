# 🧠 TerraSense: On-board Edge AI Architecture

TerraSense utilizes Edge AI to optimize downlink bandwidth by processing images on-board before transmission.

## 1. AI Pipeline Overview
1.  **Cloud Masking:** Detects and flags images with >70% cloud cover to prevent wasting downlink energy.
2.  **Region of Interest (ROI) Detection:** Automatically identifies maritime vessels or land-use changes.
3.  **Super-Resolution (Optional):** Light-weight SR models to enhance specific cropped regions.

## 2. Hardware Acceleration
- **NPU/Accelerator:** Integrated low-power AI accelerator (e.g., Myriad X or similar RISC-V based NPU).
- **Inference Latency:** <200ms for cloud masking on a 4K frame.
- **Power Draw:** <1.5W during peak inference.

## 3. Model Architecture
- **Framework:** TensorFlow Lite / ONNX Runtime.
- **Quantization:** Int8 quantization to minimize memory footprint.
- **Updateability:** AI models can be updated via UHF uplink (Patch mode).
