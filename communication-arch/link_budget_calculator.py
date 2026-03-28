import math

def calculate_link_budget(freq_mhz, dist_km, tx_power_dbm, tx_gain_db, rx_gain_db):
    """
    Calculates the RF Link Budget for Feza-X.
    Formula: Pr = Pt + Gt + Gr - Lpath - Lother
    """
    # Constant: Speed of light (m/s)
    c = 3e8
    freq_hz = freq_mhz * 1e6
    dist_m = dist_km * 1e3
    
    # 1. Path Loss (Free Space Path Loss)
    # FSPL (dB) = 20log10(d) + 20log10(f) + 20log10(4pi/c)
    fspl = 20 * math.log10(dist_m) + 20 * math.log10(freq_hz) + 20 * math.log10(4 * math.pi / c)
    
    # 2. Other Losses (Atmospheric, Connector, Pointing)
    l_other = 3.0  # Estimated 3dB loss
    
    # 3. Received Power (Pr)
    rx_power_dbm = tx_power_dbm + tx_gain_db + rx_gain_db - fspl - l_other
    
    return {
        "Frequency_MHz": freq_mhz,
        "Distance_km": dist_km,
        "FSPL_dB": round(fspl, 2),
        "Received_Power_dBm": round(rx_power_dbm, 2),
        "Link_Margin_dB": round(rx_power_dbm - (-120), 2)  # Assuming -120dBm sensitivity
    }

if __name__ == "__main__":
    # Example: S-Band Downlink (2.4 GHz) at 500km altitude
    result = calculate_link_budget(
        freq_mhz=2405, 
        dist_km=500, 
        tx_power_dbm=33, # 2W
        tx_gain_db=6,    # Patch Antenna
        rx_gain_db=20    # 3m Ground Station Dish
    )
    
    print("--- Feza-X Link Budget Analysis ---")
    for key, val in result.items():
        print(f"{key}: {val}")
