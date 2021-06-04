import matplotlib.pyplot as plt

fig = plt.figure()   # Создание объекта Figure
print (fig.axes)   # Список текущих областей рисования пуст
print (type(fig))   # тип объекта Figure
plt.scatter(1.0, 1.0)   # scatter - метод для нанесения маркера в точке (1.0, 1.0)

# После нанесения графического элемента в виде маркера
# список текущих областей состоит из одной области
print (fig.axes)

# смотри преамбулу
plt.savefig('pic_1_4_1.pdf')
plt.savefig('pic_1_4_1.png')

plt.show()
