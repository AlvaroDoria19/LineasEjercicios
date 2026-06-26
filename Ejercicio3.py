#Script usado para justificar la observación de la F/D
import numpy as np
import matplotlib.pyplot as plt


D = 1.0  # 
x = np.linspace(-D/2, D/2, 500) 


fD_ratios = [0.25, 0.5, 1.0]
colores = ['#D32F2F', '#1976D2', '#388E3C'] 
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

for fD, color in zip(fD_ratios, colores):
    f = fD * D  
    y = (x**2) / (4 * f) 
    

    ax1.plot(x, y, label=f'f/D = {fD}', color=color, linewidth=2.5)
    
 
    ax1.plot(0, f, marker='o', markersize=8, color=color)
    
    y_borde = (D/2)**2 / (4*f)
    ax1.plot([0, -D/2], [f, y_borde], '--', color=color, alpha=0.6)
    ax1.plot([0, D/2], [f, y_borde], '--', color=color, alpha=0.6)

ax1.set_title('Geometría del Reflector', fontsize=14)
ax1.set_xlabel('Posición X (m)')
ax1.set_ylabel('Posición Y (m)')
ax1.legend(loc='upper center')
ax1.grid(True, linestyle=':', alpha=0.7)
ax1.set_aspect('equal')

plt.tight_layout()
plt.show()
