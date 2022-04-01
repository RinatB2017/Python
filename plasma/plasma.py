import pygame
import math

MX = MY = 256           # Размер массива с плазмой

Pi2 = math.pi * 2.0     # Просто константа 2 * Пи для простоты и скорости

scale = 4               # Масштаб точек для вывода на экран

SX = MX * scale  # Размер экрана исходя из размера плазмы и ее масштаба
SY = MY * scale

pygame.init()
screen = pygame.display.set_mode((SX, SY))
running = True

sintab = []     # Таблица заранее просчитанных значений синусов
costab = []     # и косинусов.

                # Заполняем начальными значениями таблицы sin и cos
for index in range(0, 255):
    sintab.append(math.sin(index * Pi2 / 255.0))
    costab.append(math.cos(index * Pi2 / 255.0))

t = 0                   # Сдвиг для получения анимации
delta = Pi2 / 255.0     # Шаг нашего сдвига, на каждом кадре анимации

# -------------------------------------------------------------------------------------------------------
# Возвращаем индекс в диапазоне от 0 до 255, которое занимало бы число num, если бы его располагали от
# 0 до (2 * Пи)
# -------------------------------------------------------------------------------------------------------
def getInd(num):
    return int(((255.0 * (num % Pi2) / Pi2)))

# -------------------------------------------------------------------------------------------------------
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(0, MY):
        y = i / MY
        for j in range(0, MX):
            x = j / MX
            # Вычисляем цветовые коэффициенты и затем сами цветовые составляющие
            a1 = 8.0 * sintab[getInd(x + t)]
            a2 = 7.0 * costab[getInd(x + t)]
            a3 = 6.0 * sintab[getInd(x + t)]
            r = int(100 * abs(sintab[getInd(a1 * x + t)] + costab[getInd(a1 * y - t)]))
            g = int(100 * abs(costab[getInd(a2 * x - t)] + sintab[getInd(a2 * y + t)]))
            b = int(100 * abs(sintab[getInd(a3 * x + t)] + costab[getInd(a3 * y - t)]))
            pygame.draw.rect(screen, (r, g, b), (i*scale, j*scale, scale, scale))

    t += delta              # "Двигаем" анимацию
    if t >= Pi2:
        t = 0

    pygame.display.flip()

pygame.quit()
