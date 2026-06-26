import numpy as np
import matplotlib.pyplot as plt

# 1. Preparar dominio de datos
theta = np.linspace(0, 2*np.pi, 1000)
psi = (np.pi/2) * np.cos(theta) - (np.pi/2)

# Factor de Agrupación Normalizado
FA_psi_theta = np.abs((1 + 2*np.cos(psi)) / 3)**3

# Dominio lineal puro para FA(psi) de -pi a pi
psi_lin = np.linspace(-np.pi, np.pi, 500)
FA_psi_lin = np.abs((1 + 2*np.cos(psi_lin)) / 3)**3

# Factor de Elemento (Dipolo en X) evaluado en Plano E (Plano XZ)
FE = np.zeros_like(theta)
for i, t in enumerate(theta):
    # Evitar singularidad en theta = pi/2 y 3pi/2
    if np.isclose(t, np.pi/2) or np.isclose(t, 3*np.pi/2):
        FE[i] = 0
    else:
        FE[i] = np.abs(np.cos(np.pi/2 * np.sin(t)) / np.cos(t))

# Diagramas Totales
Plano_H = FA_psi_theta * 1  # FE = 1 en plano YZ
Plano_E = FA_psi_theta * FE

# 2. Crear las gráficas
fig = plt.figure(figsize=(14, 10))

# Gráfico 1: FA(psi) Lineal
ax1 = fig.add_subplot(221)
ax1.plot(psi_lin * (180/np.pi), FA_psi_lin, 'b', lw=2)
ax1.set_title(r'FA($\psi$) Lineal')
ax1.set_xlabel(r'$\psi$ (grados)')
ax1.set_ylabel('Amplitud Normalizada')
ax1.grid(True)
ax1.set_xlim(-180, 180)

# Gráfico 2: FA(theta) Polar
ax2 = fig.add_subplot(222, polar=True)
ax2.plot(theta, FA_psi_theta, 'r', lw=2)
ax2.set_title(r'FA($\theta$) Polar (Antenas Isotrópicas)')
ax2.set_theta_zero_location("N") # Z-axis pointing up
ax2.set_theta_direction(-1)

# Gráfico 3: Plano H Polar
ax3 = fig.add_subplot(223, polar=True)
ax3.plot(theta, Plano_H, 'g', lw=2)
ax3.set_title('Plano H (Plano YZ)')
ax3.set_theta_zero_location("N")
ax3.set_theta_direction(-1)

# Gráfico 4: Plano E Polar
ax4 = fig.add_subplot(224, polar=True)
ax4.plot(theta, Plano_E, 'm', lw=2)
ax4.set_title('Plano E (Plano XZ)')
ax4.set_theta_zero_location("N")
ax4.set_theta_direction(-1)

plt.tight_layout()
plt.show()
