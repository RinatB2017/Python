import matplotlib.pyplot as plt
import numpy as np

N = 100
x = np.arange(N)
# Задаём выборку из Гамма-распредления с параметрами формы=1. и масштаба=0.
z = np.random.gamma(2., 1., N)
z1 = np.cos(x/10.)
z2 = np.cos(x/20.)

y = z.reshape(10,10)
#y = np.cos(y)

fig = plt.figure()
cc = plt.contourf(y) 
cbar = plt.colorbar(cc)

plt.title('1. TITLE', color='green')
plt.xlabel('2. X - LABEL')
plt.ylabel('3. Y - LABEL', fontsize=16)

# Подписи для цветовых шкал имеют отличный от остальных подписей синтаксис
cbar.ax.set_xlabel('4. COLORBAR X-LABEL', color='b')
cbar.ax.set_ylabel('5. COLORBAR Y-LABEL', color='r')
plt.grid(True)

fig = plt.figure()

my_dict = {'color' : 'grey', 'linewidth' : 2.5, 'linestyle' : '--'}
xz = [x, z]

# передача параметров через список xz и словарь my_dict. Наличие знаков * и ** обязательно!
cc = plt.plot(*xz, **my_dict) 
# результат аналогичен такой записи
#cc = plt.plot(x, z, color='grey', linewidth=2.5, linestyle='--')

plt.scatter(x, y + 2.0, marker='v', s=10, color='red')

plt.title('Sample from Gamma distribution')
plt.xlabel('Gamma sample values')
plt.ylabel('Sample numbers')

# Подписи для цветовых шкал имеют отличный от остальных подписей синтаксис
cbar.ax.set_xlabel('4. COLORBAR X-LABEL', fontsize=8)
cbar.ax.set_ylabel('5. COLORBAR Y-LABEL', color='r')
plt.grid(True, color='blue', linewidth=1.0)

fig = plt.figure()

# создание словаря
my_dict = {'color' : 'green', 'linewidth' : 4.0, 'alpha' : 0.5} 

plt.fill_between(x, z2, z1, color='green', alpha=0.25) 
plt.plot(x, z1, color='green', linewidth=4.0)
plt.plot(x, z2, **my_dict)
plt.title('Different alpha values')
plt.grid(True)

# смотри преамбулу
plt.savefig('pic_1_6_2.pdf')
plt.savefig('pic_1_6_2.png')

plt.show()
