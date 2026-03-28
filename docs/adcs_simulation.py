import time

class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.prev_error = 0
        self.integral = 0

    def compute(self, setpoint, current_value, dt):
        error = setpoint - current_value
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt
        output = (self.kp * error) + (self.ki * self.integral) + (self.kd * derivative)
        self.prev_error = error
        return output

def simulate_adcs_nadir_pointing():
    """
    Simulates a simple 1-axis Nadir pointing control for Feza-X.
    Goal: Align Z-axis with NADIR (0 degrees error).
    """
    print("[*] Starting Feza-X ADCS Simulation (Nadir Pointing)...")
    
    # PID Gains (Tuned for CubeSat inertia)
    pid = PIDController(kp=0.5, ki=0.01, kd=0.2)
    
    current_angle = 15.0  # Initial 15 degree offset
    target_angle = 0.0    # Desired Nadir pointing
    dt = 0.1              # 100ms control loop
    
    for i in range(50):
        torque = pid.compute(target_angle, current_angle, dt)
        
        # Simple Physics: Angle changes based on torque (simplified)
        current_angle += torque * dt
        
        print(f"Step {i}: Current Angle = {current_angle:.4f} | Torque Output = {torque:.4f}")
        time.sleep(0.01)

if __name__ == "__main__":
    simulate_adcs_nadir_pointing()
