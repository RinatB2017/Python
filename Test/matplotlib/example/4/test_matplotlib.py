import matplotlib.pyplot as plt
import numpy as np

N = 100
n = np.sqrt(N)
x = np.arange(n)
# Задаём выборку из Гамма-распредления с параметрами формы=1. и масштаба=0.
z = np.random.random(N).reshape(n, n)
y = z[5,:]

fig = plt.figure()
cc = plt.contourf(z, alpha=0.5)   # трёхмерное поле
plt.plot(x, y, label='line', color='red') # красная линия

plt.title('1a. Title')   # заголовок
plt.xlabel('2a. Xlabel')   # подпись оси OX
plt.ylabel('3a. Ylabel')   # подпись оси OY
plt.legend()   # легенда
cbar = plt.colorbar(cc)   # цветовая шкала

plt.text(2.5, 7, '1. Axes', fontsize=26, bbox=dict(edgecolor='w', color='w'))
plt.text(4, -0.5, '2. XAxis', fontsize=18, bbox=dict(edgecolor='w', color='w'))
plt.text(-0.5, 3.8, '3. YAxis', fontsize=18, bbox=dict(edgecolor='w', color='w'), rotation=90)
plt.text(6.3, 7.2, '4. Legend', fontsize=16, bbox=dict(edgecolor='w', color='w'))
plt.text(9.1, 5., '5. Colorbar', fontsize=16, bbox=dict(edgecolor='w', color='w'), rotation=90)
plt.text(7., 0.8, '6. Xticks', fontsize=12, bbox=dict(edgecolor='w', color='w'))
plt.text(0.8, 8.4, '7. Yticks', fontsize=12, bbox=dict(edgecolor='w', color='w'), rotation=90)

# Подписи для цветовых шкал имеют отличный от остальных подписей синтаксис
cbar.ax.set_xlabel('5a. Colorbar Xlabel', color='k', rotation=30)
cbar.ax.set_ylabel('5b. Colorbar Ylabel', color='k')

plt.text(2.8, 4.8,'6. Grid lines', fontsize=14)
plt.grid(True)

# смотри преамбулу
#save('pic_1_5_2', fmt='pdf')
#save('pic_1_5_2', fmt='png')

plt.show()
