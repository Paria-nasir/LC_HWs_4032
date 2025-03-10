import numpy as np
import matplotlib.pyplot as plt

def simulate_pitch_dynamics(dt=0.01, total_time=5, control_inputs=[-5, 0, 10]):
    a1, a2, a3 = -8.79, -2.075, -11.87
    t_vals = np.arange(0, total_time, dt)
    theta_vals, theta_rate_vals = np.zeros(len(t_vals)), np.zeros(len(t_vals))
    plt.figure(figsize=(10, 5))
    
    for ctrl in control_inputs:
        for i in range(1, len(t_vals)):
            theta_acc = a1 * theta_vals[i-1] + a2 * theta_rate_vals[i-1] + a3 * np.deg2rad(ctrl)
            theta_rate_vals[i] = theta_rate_vals[i-1] + dt * theta_acc
            theta_vals[i] = theta_vals[i-1] + dt * theta_rate_vals[i-1]
        plt.plot(t_vals, np.rad2deg(theta_vals), label=f'Input = {ctrl}°')
    
    plt.xlabel('Time (seconds)')
    plt.ylabel('Pitch Angle (degrees)')
    plt.title('Pitch Motion Response')
    plt.legend()
    plt.grid()
    plt.show()

simulate_pitch_dynamics()