# TerraSense: Mission Control Center (MCC) Environment
# Usage: docker build -t terrasense-mcc . && docker run -it terrasense-mcc

FROM python:3.10-slim

# 1. Install System Dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# 2. Set Working Directory
WORKDIR /app

# 3. Copy MCC Tools
COPY docs/pass_calculator.py /app/
COPY communication-arch/telemetry_dictionary.json /app/

# 4. Install Mission Core Libraries
RUN pip install --no-cache-dir \
    skyfield \
    numpy \
    influxdb-client \
    pyserial \
    crcmod

# 5. Default Command: Start the Pass Calculator
CMD ["python", "pass_calculator.py"]
