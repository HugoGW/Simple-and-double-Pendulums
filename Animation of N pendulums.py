import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.animation import FuncAnimation

# Length of the pendulum (m)
L = 1.0
# Mass of the pendulum (kg)
m = 1.0
# Gravitational acceleration (m/s^2)
g = 9.81

# Function that solves ODE using odeint
def solve_ODE(equation, f0, t_values, column):
    solution = odeint(equation, f0, t_values)
    f_values = solution[:, column]
    return f_values

# Function representing the differential equation for the simple pendulum
def Eq_SP(y, t):
    theta, theta_dot = y

    # Differential equation for θ
    theta_double_dot = -g / L * np.sin(theta)

    return [theta_dot, theta_double_dot]

# Number of pendulums
N_pend = 1

# Initial conditions
dθ = np.radians(0.0001)
dω = np.radians(0.0)
θ_0 = np.radians(90)
ω_0 = np.radians(0)
θ_init = [[θ_0 + i * dθ, ω_0 + i * dω] for i in range(N_pend)]

# Time interval for the simulation
t_start = 0.0
t_end = 15.0
t_values = np.arange(t_start, t_end, 0.01)

# Solving the differential equations for the N pendulums
θ = [solve_ODE(Eq_SP, θ_0, t_values, 0) for θ_0 in θ_init]

# Cartesian coordinates for each pendulum
x = [L * np.sin(θ_i) for θ_i in θ]
y = [-L * np.cos(θ_i) for θ_i in θ]

# Animation of the N simple pendulums with a point at the end and a fine trail
fig, ax = plt.subplots()
points = [plt.plot([], [], 'o', markersize=6)[0] for _ in range(N_pend)]
lines = [plt.plot([], [], lw=0.5)[0] for _ in range(N_pend)]
trails = [plt.plot([], [], '-', lw=1, alpha=0.5)[0] for _ in range(N_pend)]

def init():
    for point, trail, line in zip(points, trails, lines):
        ax.set_xlim(-L*1.1, L*1.1)
        ax.set_ylim(-L*1.1, L*1.1)
        ax.set_aspect('equal')
        point.set_data([], [])
        trail.set_data([], [])
        line.set_data([], [])
    return points + trails + lines

def animate(i):
    for j in range(N_pend):
        points[j].set_data(x[j][i], y[j][i])
        trails[j].set_data(x[j][:i+1], y[j][:i+1])
        lines[j].set_data([0, x[j][i]], [0, y[j][i]])
    return points + trails + lines

ani = FuncAnimation(fig, animate, frames=len(t_values), init_func=init, interval=1)
plt.title(f'Animation of {N_pend} simple pendulum(s)')
plt.show()
