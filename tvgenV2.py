import numpy as np

# Константы
k = 64
chastota = 10
period = 1 / chastota
hmicros = k
a = 625
b = 12.0
c = 1.5
d = 4.7
y = c + d
z = d / 2
cbstart = c + 5.6
cbstop = cbstart + 2.2

# Битовые маски
sync = 0b00000000
black = 0b00000001
fh2 = 0b00000010
cb = 0b00000101
white = 0b00111001
blue = 0b00001001
green = 0b00010001
red = 0b00100001
yellow = red | green
cyan = blue | green
magneta = blue | red
ctrl = 0b01000000
reset = 0b10000001
databit = 0b00000000

# Открываем файл для записи
f = open('FRAME.bin', 'wb')

# Универсальная функция для генерации строки сигнала
def generate_signal_line(start, end, color=black, fh2_flag=False):
    for i in np.arange(start, end, period):
        databit2 = 0
        databit = 0
        # Условия для генерации сигнала
        if 0 < i < c:
            databit = black
        elif c < i < y:
            databit = sync
        elif y < i < cbstart:
            databit = black
        elif cbstart < i < cbstop:
            databit = cb
        elif cbstop < i < b:
            databit = black
        elif i > b:
            databit = color

        # Добавляем fh2, если флаг установлен
        databit2 = databit | fh2 if fh2_flag else databit
        f.write(databit2.to_bytes(1, byteorder='big'))

# Функция для генерации строк с цветом
def generate_color_line(start, end, color, fh2_flag=False):
    for i in np.arange(start, end, period):
        databit2 = 0
        databit = 0

        # Условия для генерации сигнала
        if 0 < i < c:
            databit = black
        elif c < i < y:
            databit = sync
        elif y < i < cbstart:
            databit = black
        elif cbstart < i < cbstop:
            databit = cb
        elif cbstop < i < b:
            databit = black
        elif i > b:
            databit = color

        # Добавляем fh2, если флаг установлен
        databit2 = databit | fh2 if fh2_flag else databit
        f.write(databit2.to_bytes(1, byteorder='big'))

# Функция для генерации строк с контрольными сигналами
def generate_control_line(start, end, color, fh2_flag=False):
    for i in np.arange(start, end, period):
        databit = 0 
        databit2 = 0

        # Условия для генерации сигнала
        if 0 < i < c:
            databit = black
        elif c < i < y:
            databit = sync
        elif y < i < cbstart:
            databit = black
        elif cbstart < i < cbstop:
            databit = cb
        elif cbstop < i < b:
            databit = black
        elif i > b:
            databit = color | ctrl

        # Добавляем fh2, если флаг установлен
        databit2 = databit | fh2 if fh2_flag else databit
        f.write(databit2.to_bytes(1, byteorder='big'))

# Основной цикл для генерации строк
g = 0
while g < a + 1:
    if 0 < g < 3:
        generate_signal_line(0, hmicros, black)
        print('stroki1_2')
    elif g == 3:
        generate_signal_line(0, hmicros, black)
        print('stroka3')
    elif 3 < g < 6:
        generate_signal_line(0, hmicros, black)
        print('stroka4_5')
    elif 5 < g < 25:
        if g % 2 == 0:
            generate_signal_line(0, hmicros, black)
        else:
            generate_signal_line(0, hmicros, black, fh2_flag=True)
        print('stroka6_24')
    elif 24 < g < 41:
        if g % 2 == 0:
            generate_color_line(0, hmicros, blue)
        else:
            generate_color_line(0, hmicros, blue, fh2_flag=True)
    elif 40 < g < 57:
        if g % 2 == 0:
            generate_color_line(0, hmicros, red)
        else:
            generate_color_line(0, hmicros, red, fh2_flag=True)
    elif 56 < g < 65:
        if g % 2 == 0:
            generate_color_line(0, hmicros, yellow)
        else:
            generate_color_line(0, hmicros, yellow, fh2_flag=True)
    elif 64 < g < 169:
        if g % 2 == 0:
            generate_color_line(0, hmicros, green)
        else:
            generate_color_line(0, hmicros, green, fh2_flag=True)
    elif 168 < g < 177:
        if g % 2 == 0:
            generate_signal_line(0, hmicros, black)
        else:
            generate_signal_line(0, hmicros, black, fh2_flag=True)
    elif 176 < g < 193:
        if g % 2 == 0:
            generate_control_line(0, hmicros, red)
        else:
            generate_control_line(0, hmicros, red, fh2_flag=True)
    elif 192 < g < 201:
        if g % 2 == 0:
            generate_control_line(0, hmicros, yellow)
        else:
            generate_control_line(0, hmicros, yellow, fh2_flag=True)
    elif 200 < g < 305:
        if g % 2 == 0:
            generate_control_line(0, hmicros, green)
        else:
            generate_control_line(0, hmicros, green, fh2_flag=True)
    elif 304 < g < 311:
        if g % 2 == 0:
            generate_signal_line(0, hmicros, black)
        else:
            generate_signal_line(0, hmicros, black, fh2_flag=True)
    elif 310 < g < 313:
        generate_signal_line(0, hmicros, black)
        print('stroka311_312')
    elif g == 313:
        generate_signal_line(0, hmicros, black)
        print('stroka313')
    elif 313 < g < 316:
        generate_signal_line(0, hmicros, black)
        print('stroki314_315')
    elif 315 < g < 318:
        generate_signal_line(0, hmicros, black)
        print('stroka316_317')
    elif g == 318:
        generate_signal_line(0, hmicros, black)
        print('stroka318')
    elif 318 < g < 336:
        if g % 2 == 0:
            generate_signal_line(0, hmicros, black)
        else:
            generate_signal_line(0, hmicros, black, fh2_flag=True)
        print('stroki319_336')
    elif 335 < g < 352:
        if g % 2 == 0:
            generate_color_line(0, hmicros, blue)
        else:
            generate_color_line(0, hmicros, blue, fh2_flag=True)
    elif 351 < g < 368:
        if g % 2 == 0:
            generate_control_line(0, hmicros, red)
        else:
            generate_control_line(0, hmicros, red, fh2_flag=True)
    elif 367 < g < 376:
        if g % 2 == 0:
            generate_control_line(0, hmicros, yellow)
        else:
            generate_control_line(0, hmicros, yellow, fh2_flag=True)
    elif 375 < g < 480:
        if g % 2 == 0:
            generate_control_line(0, hmicros, green)
        else:
            generate_control_line(0, hmicros, green, fh2_flag=True)
    elif 479 < g < 488:
        if g % 2 == 0:
            generate_signal_line(0, hmicros, black)
        else:
            generate_signal_line(0, hmicros, black, fh2_flag=True)
    elif 487 < g < 504:
        if g % 2 == 0:
            generate_control_line(0, hmicros, red)
        else:
            generate_control_line(0, hmicros, red, fh2_flag=True)
    elif 503 < g < 512:
        if g % 2 == 0:
            generate_control_line(0, hmicros, yellow)
        else:
            generate_control_line(0, hmicros, yellow, fh2_flag=True)
    elif 511 < g < 616:
        if g % 2 == 0:
            generate_control_line(0, hmicros, green)
        else:
            generate_control_line(0, hmicros, green, fh2_flag=True)
    elif 615 < g < 623:
        if g % 2 == 0:
            generate_signal_line(0, hmicros, black)
        else:
            generate_signal_line(0, hmicros, black, fh2_flag=True)
    elif g == 623:
        generate_signal_line(0, hmicros, black)
        print('stroka623')
    elif g == 624:
        generate_signal_line(0, hmicros, black)
        print('stroka624')
    elif g == 625:
        generate_signal_line(0, hmicros, black)
        print('stroka625')

    print(g)
    g += 1

f.close()
