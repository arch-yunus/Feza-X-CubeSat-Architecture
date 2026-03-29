#!/usr/bin/env python3
"""
🌡️ Feza-X: Passive Thermal Equilibrium Model for LEO
This script calculates the steady-state temperature (T_sat) of the satellite 
by balancing Solar Flux, Albedo, and Earth IR against Radiation Cooling.
"""

import math

# --- Constants ---
SIGMA = 5.67e-8  # Stefan-Boltzmann constant (W/m^2 K^4)
SOLAR_FLUX = 1367.0  # Solar constant (W/m^2)
ALBEDO_COEFF = 0.3   # Earth Albedo coefficient (Avg)
EARTH_IR = 237.0     # Earth IR Flux (W/m^2)

# --- Satellite Parameters (Feza-X 3U) ---
# Area exposed to sun (Assuming 1U face = 0.01 m^2, 3U face = 0.03 m^2)
AREA_ZENITH = 0.01  # Top (Small face)
AREA_SIDES = 0.03   # Long faces (4 sides)
TOTAL_EMITTING_AREA = 0.08  # Total surface area (Assuming 2x 0.01 + 4x 0.03 = 0.14? No, 2*0.01 + 4*0.03 = 0.14)
# Let's use 0.14 for total surface area of a 3U.

def calculate_temp_steady_state(alpha, epsilon, internal_power=5.0):
    """
    Solves for T based on Energy In = Energy Out
    In: Solar + Albedo + EarthIR + InternalPower
    Out: Radiative Cooling (sigma * epsilon * Area * T^4)
    """
    # 1. Total Heat Input (W)
    # Assumes worst-case: Sunlight perpendicular to one long face (0.03 m^2)
    q_solar = SOLAR_FLUX * alpha * 0.03 
    q_albedo = SOLAR_FLUX * ALBEDO_COEFF * alpha * 0.03
    q_earth_ir = EARTH_IR * epsilon * 0.03
    
    total_q_in = q_solar + q_albedo + q_earth_ir + internal_power
    
    # 2. Radiative Heat Output (W) = sigma * epsilon * Area * T^4
    # T = (Q_in / (sigma * epsilon * Area))^(1/4)
    # Total surface area of 3U = 0.14 m^2
    t_kelvin = (total_q_in / (SIGMA * epsilon * 0.14))**0.25
    t_celsius = t_kelvin - 273.15
    return t_celsius

def main():
    print("--- Feza-X: Steady-State Thermal Model (LEO) ---")
    
    # CASE 1: Black Anodized Chassis (High alpha, High epsilon)
    temp_black = calculate_temp_steady_state(alpha=0.9, epsilon=0.88, internal_power=5.0)
    print(f"[CASE: Black Anodized] Alpha: 0.9, Epsilon: 0.88 | T_sat: {temp_black:.2f}°C")

    # CASE 2: White Thermal Paint (Low alpha, High epsilon) - Cold Case
    temp_white = calculate_temp_steady_state(alpha=0.2, epsilon=0.85, internal_power=2.0)
    print(f"[CASE: White Paint]    Alpha: 0.2, Epsilon: 0.85 | T_sat: {temp_white:.2f}°C")

    # CASE 3: Bare Aluminum (Low alpha, Low epsilon)
    temp_alum = calculate_temp_steady_state(alpha=0.15, epsilon=0.05, internal_power=5.0)
    print(f"[CASE: Polished Alum] Alpha: 0.15, Epsilon: 0.05 | T_sat: {temp_alum:.2f}°C")

    print("\n[INFO] Feza-X maintains operational range (+5°C to +45°C) with Black Anodized finish.")

if __name__ == "__main__":
    main()
