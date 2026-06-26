#Script de Python del Ejercicio 1, Inciso B
import numpy as np
import matplotlib.pyplot as plt

a = 20  # Ancho total en el eje X
b = 10  # Ancho total en el eje Y
x = np.linspace(-a/2, a/2, 500)
y = np.linspace(-b/2, b/2, 500)
E_x = np.cos(np.pi * x / a)         
E_y = 1 - np.abs(y) / (b / 2)        

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 7))
fig.suptitle('Distribución de Campo en Apertura de Antena', fontsize=16)

ax1.plot(x, E_x, color='#1A66CC', linewidth=2) 
ax1.fill_between(x, E_x, color='#E6EFFF')      
ax1.set_title('Distribución Cosenoidal (Plano H / Eje X)', fontsize=14, fontweight='bold', loc='left', pad=10)
ax1.set_ylabel('Amplitud Relativa ↑', fontsize=9, color='gray')
ax1.set_xlim([-10, 10])
ax1.set_ylim([0, 1.1])
ax1.grid(True, linestyle='-', color='lightgray')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

ax2.plot(y, E_y, color='#1A731A', linewidth=2)
ax2.fill_between(y, E_y, color='#E6F2E6')   
ax2.set_title('Distribución Triangular (Plano E / Eje Y)', fontsize=14, fontweight='bold', loc='left', pad=10)
ax2.set_ylabel('Amplitud Relativa ↑', fontsize=9, color='gray')
ax2.set_xlim([-5, 5])
ax2.set_ylim([0, 1.1])
ax2.grid(True, linestyle='-', color='lightgray')
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
plt.tight_layout()
fig.subplots_adjust(top=0.88) # Dar espacio al título principal
plt.show()
