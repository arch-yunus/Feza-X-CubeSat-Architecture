#!/usr/bin/env python3
"""
🛰️ Feza-X: CubeSat Space Protocol (CSP) Packet Generator v1.0
This script simulates the generation of CSP headers for testing communication interfaces.
"""

import struct

class CSPPacket:
    def __init__(self, priority=1, source=1, destination=2, dest_port=10, flags=0):
        self.priority = priority    # 2 bits
        self.source = source        # 5 bits
        self.destination = destination # 5 bits
        self.dest_port = dest_port  # 6 bits
        self.flags = flags          # 8 bits
        # Reserved: 6 bits (total 32 bits)

    def encode_header(self):
        """Encodes CSP v1.x header into a 32-bit unsigned integer."""
        header = 0
        header |= (self.priority & 0x03) << 30
        header |= (self.source & 0x1F) << 25
        header |= (self.destination & 0x1F) << 20
        header |= (self.dest_port & 0x3F) << 14
        header |= (self.flags & 0xFF) << 6
        return header

    def to_hex(self):
        """Returns the hex representation of the 4-byte header."""
        return f"0x{self.encode_header():08X}"

def main():
    print("--- Feza-X: CSP Packet Generator Simulator ---")
    
    # 1. Housekeeping Request (Ping)
    ping = CSPPacket(priority=2, source=1, destination=2, dest_port=1, flags=0x01)
    print(f"[PING] OBC -> EPS (Port 1): {ping.to_hex()}")

    # 2. Critical Science Data (High Priority)
    telemetry = CSPPacket(priority=0, source=3, destination=1, dest_port=31, flags=0x00)
    print(f"[DATA] Payload -> OBC (Port 31): {telemetry.to_hex()}")

    # 3. Ground Command (Encrypted Flag)
    command = CSPPacket(priority=3, source=10, destination=1, dest_port=10, flags=0x80)
    print(f"[CMD] GS -> OBC (Port 10, Encrypted): {command.to_hex()}")

    print("\n[INFO] CSP Headers generated successfully for Feza-X Bus verification.")

if __name__ == "__main__":
    main()
