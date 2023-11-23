import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Função para representar um cone
def cone(x, y):
    z = np.sqrt(x**2 + y**2)
    return z

# Função para representar uma montanha
def montanha(x, y):
    z = np.sin(np.sqrt(x**2 + y**2))
    return z

# Criando a grade de pontos
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

# Calculando os valores das funções nos pontos da grade
z_cone = cone(x, y)
z_montanha = montanha(x, y)

# Criando figuras 3D para as superfícies
fig_cone = plt.figure(figsize=(8, 6))
ax_cone = fig_cone.add_subplot(111, projection='3d')
ax_cone.plot_surface(x, y, z_cone, cmap='viridis')
ax_cone.set_title('Superfície do Cone')


fig_montanha = plt.figure(figsize=(8, 6))
ax_montanha = fig_montanha.add_subplot(111, projection='3d')
ax_montanha.plot_surface(x, y, z_montanha, cmap='viridis')
ax_montanha.set_title('Superfície da Montanha')


# Exibindo os gráficos
plt.show()
