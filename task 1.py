import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.special import jn_zeros, j0, j1
from scipy.integrate import quad


A = 1.0
omega = 2.0
a = 1.0
N_terms = 15


mu_k = jn_zeros(0, N_terms)
C_k = np.zeros(N_terms)

for i, mu in enumerate(mu_k):
    integral_val, _ = quad(lambda r: r * j1(mu * r), 0, 1)
    
    numerator = j1(mu) - integral_val
    denominator = j1(mu)**2
    C_k[i] = (2 * A / mu) * (numerator / denominator)


r_arr = np.linspace(0, 1, 50)
phi_arr = np.linspace(0, 2 * np.pi, 50)
R, Phi = np.meshgrid(r_arr, phi_arr)


X = R * np.cos(Phi)
Y = R * np.sin(Phi)


def calculate_z(R_grid, t):
    """Вычисляет отклонение мембраны Z(r, t) в заданный момент времени."""
    Z = np.zeros_like(R_grid)
    for i, mu in enumerate(mu_k):
        term_time = (C_k[i] / ((a * mu)**2 - omega**2)) * \
                    (np.sin(omega * t) - (omega / (a * mu)) * np.sin(a * mu * t))
        term_space = j0(mu * R_grid)
        
        Z += term_time * term_space
    return Z


fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

t_frames = np.linspace(0, 10, 150)

def update(frame):
    ax.clear()
    
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-0.9, 0.9)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Смещение U(r,t)')
    ax.set_title(f'Вынужденные колебания мембраны (Время t = {frame:.2f})')
    
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    
    Z = calculate_z(R, frame)
    surf = ax.plot_surface(X, Y, Z, cmap='plasma', rstride=1, cstride=1, 
                           edgecolor='none', alpha=0.9)
    return surf,

ani = FuncAnimation(fig, update, frames=t_frames, interval=50, blit=False)

plt.show()

# ani.save('membrane_vibration.mp4', writer='ffmpeg', fps=30)