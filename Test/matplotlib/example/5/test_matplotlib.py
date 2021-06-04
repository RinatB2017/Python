import matplotlib.pyplot as plt
import numpy as np

# Пример функции с объединением в кортеж *args
def f_sums(*args):

    list1 = []
    for arg in args:
        a = 0
        for i in arg:
            a += i
        list1.append(a)

    return list1

# Пример функции с объединением в словарь **kwargs
def f_words(**kwargs):
    '''
    Функция pop возвращает значение для заданного ключа (если он есть в словаре)
    и удаляет из словаря пару "ключ - значение"
    '''
    
    print ('Словарь kwargs ДО вызова метода pop:', kwargs)
    per1 = kwargs.pop('solo', 'Han')
    per2 = kwargs.pop('wookie', 'Chubbaca')
    act = kwargs.pop('loves', 'loves')
    str1 = '%s %s %s' % (per1, act, per2)
    print ('Словарь kwargs ПОСЛЕ вызова метода pop:', kwargs)
    
    return str1

# Пример функции с объединением и в кортеж args и в словарь **kwargs
def f_plot(*args, **kwargs):

    xlist = []
    ylist = []
    for i, arg in enumerate(args):
        if(i % 2 == 0):
            xlist.append(arg)
        else:
            ylist.append(arg) 
    
    colors = kwargs.pop('colors', 'k')
    linewidth = kwargs.pop('linewidth', 1.)
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    i = 0
    for x, y, color in zip(xlist, ylist, colors):
        i += 1
        ax.plot(x, y, color=color, linewidth=linewidth, label=str(i))
    
    ax.grid(True)
    ax.legend()
    plt.savefig('ex_1_6_1.pdf')
    plt.savefig('ex_1_6_1.png')

# ==================================
# MAIN SCRIPT BODY

x = np.arange(10)
y = np.random.random(20)
z = np.linspace(-15, -7.5, 37)
xyz = [x, y, z]

abc = {'solo': 1, 'wookie': 'green', 'friend': True}

res1 = f_sums(*xyz)
res2 = f_words(**abc)

print ('res1', type(res1), res1)
print ('res2', type(res2), res2)

"""
Т.к. в plt.plot нет обязательных параметров, то переданные 
в эту функцию через зпт последовательности или массивы будут обработаны
Здесь пример передачи двух линий - две последовательности из пары OX-OY
(x, y2) и (x, y3). Им в соответствие представлена последовательность цветов
colors.
"""
colors = ['red', 'blue']
N = 10
x = np.arange(N)
y2 = np.random.random(N)
y3 = np.random.random(N)

f_plot(x, y2, x , y3, colors=colors, linewidth=2.)
