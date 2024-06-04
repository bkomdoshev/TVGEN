import numpy as np

j = 0
i: float = 0.0
l: float = 0.0
m = 0
o = 0
p = 0
q = 0
r = 0
s = 0
t = 0
u = 0
n = 0
v = 0
x = 0
#ch = 0
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


k = 64
chastota = 10 # MHz
period = 1 / chastota
hmicros = k + period
a = 625
b: float = 12
c: float = 1.5
d: float = 4.7
y: float = 6.2
z: float = 2.35
cbstart: float = c + 5.6
cbstop: float = cbstart + 2.2
g = 0
f = open('FIRMWAR.bin', 'wb')
# EEPROM OUTS:                      PALMOD EEPROM ADDRESS: 
# D1) SYNC BLACK LEVEL              A2
# D2) FH/2 128usec                  A3
# D3) STB colorburst                A7
# D4) Blue                          A4
# D5) Green                         A5
# D6) Red                           A6
# D7) Control clock  multiplexor
# D8) Reset  
def stroka_signala_8_chet():
    for i in np.arange(period, hmicros, period):
        databit2 = 0
        if 0<i < c+period:
            databit = black 

        if c < i < y+period:
            databit = sync

        if y < i < cbstart+period:
            databit = black

        if cbstart < i < cbstop+period:    
            databit = cb

        if cbstop < i < b+period:
            databit = black
            
        if i > b:
            databit = black

        databit2 = databit
        f.write(databit2.to_bytes(1, byteorder='big'))
        
def stroka_signala_8_nechet():
    for i in np.arange(period, hmicros, period):
        databit2 = 0
        if 0<i < c+period:
           databit = black

        if c < i < y+period:
           databit = sync

        if  y < i < cbstart+period:
            databit = black

        if  cbstart < i < cbstop+period:    
            databit = cb

        if cbstop < i < b+period:
            databit = black

        if i > b:
            databit = black
        databit2 = databit|fh2
        f.write(databit2.to_bytes(1, byteorder='big'))
        
def stroka_signala_16_chet():
    for i in np.arange(period, hmicros, period):
        databit2 = 0
        if 0<i < c+period:
            databit = black 

        if c < i < y+period:
            databit = sync

        if y < i < cbstart+period:
            databit = black

        if cbstart < i < cbstop+period:    
            databit = cb

        if cbstop < i < b+period:
            databit = black
            
        if i > b:
            databit = blue

        databit2 = databit
        f.write(databit2.to_bytes(1, byteorder='big'))
        
def stroka_signala_16_nechet():
    for i in np.arange(period, hmicros, period):
        databit2 = 0
        if 0<i < c+period:
           databit = black

        if c < i < y+period:
           databit = sync

        if  y < i < cbstart+period:
            databit = black

        if  cbstart < i < cbstop+period:    
            databit = cb

        if cbstop < i < b+period:
            databit = black

        if i > b:
            databit = blue
        databit2 = databit|fh2
        f.write(databit2.to_bytes(1, byteorder='big'))
                          
def stroka_signala_red_chet():
    for i in np.arange(period, hmicros, period):
        databit2 = 0
        if 0<i < c+period:
            databit = black 

        if c < i < y+period:
            databit = sync

        if y < i < cbstart+period:
            databit = black

        if cbstart < i < cbstop+period:    
            databit = cb

        if cbstop < i < b+period:
            databit = black
#kanaly1-2
        if 14.4 > i > b:
            databit = black
        if 16.4 > i > 14.4:
            databit = red|ctrl
        if 17.2 > i > 16.4:
            databit = black
        if 19.2 > i > 17.2:
            databit = red|ctrl
        if 20.4 > i > 19.2:
            databit = black
#kanaly3-4
        if 22.4 > i > 20.4:
            databit = red|ctrl
        if 23.2 > i > 22.4:
            databit = black
        if 25.2 > i > 23.2:
            databit = red|ctrl
        if 26.4 > i > 25.2:
            databit = black
#kanaly5-6
        if 28.4 > i > 26.4:
            databit = red|ctrl
        if 29.2 > i > 28.4:
            databit = black
        if 31.2 > i > 29.2:
            databit = red|ctrl
        if 32.4 > i > 31.2:
            databit = black
#kanaly7-8
        if 34.4 > i > 32.4:
            databit = red|ctrl
        if 35.2 > i > 34.4:
            databit = black
        if 37.2 > i > 35.2:
            databit = red|ctrl
        if 38.4 > i > 37.2:
            databit = black
#kanaly9-10
        if 40.4 > i > 38.4:
            databit = red|ctrl
        if 41.2 > i > 40.4:
            databit = black
        if 43.2 > i > 41.2:
            databit = red|ctrl
        if 44.4 > i > 43.2:
            databit = black
#kanaly11-12
        if 46.4 > i > 44.4:
            databit = red|ctrl
        if 47.2 > i > 46.4:
            databit = black
        if 49.2 > i > 47.2:
            databit = red|ctrl
        if 50.4 > i > 49.2:
            databit = black  
#kanaly13-14
        if 52.4 > i > 50.4:
            databit = red|ctrl
        if 53.2 > i > 52.4:
            databit = black
        if 55.2 > i > 53.2:
            databit = red|ctrl
        if 56.4 > i > 55.2:
            databit = black
#kanaly15-16
        if 58.4 > i > 56.4:
            databit = red|ctrl
        if 59.2 > i > 58.4:
            databit = black
        if 61.2 > i > 59.2:
            databit = red|ctrl 
        if i > 61.2:
            databit = black
          
        databit2 = databit
        f.write(databit2.to_bytes(1, byteorder='big'))

def stroka_signala_red_nechet():
    for i in np.arange(period, hmicros, period):
        databit2 = 0
        if 0<i < c+period:
           databit = black

        if c < i < y+period:
           databit = sync

        if  y < i < cbstart+period:
            databit = black

        if  cbstart < i < cbstop+period:    
            databit = cb
            
        if cbstop < i < b+period:
            databit = black
#kanaly1-2
        if 14.4 > i > b:
            databit = black
        if 16.4 > i > 14.4:
            databit = red|ctrl
        if 17.2 > i > 16.4:
            databit = black
        if 19.2 > i > 17.2:
            databit = red|ctrl
        if 20.4 > i > 19.2:
            databit = black
#kanaly3-4
        if 22.4 > i > 20.4:
            databit = red|ctrl
        if 23.2 > i > 22.4:
            databit = black
        if 25.2 > i > 23.2:
            databit = red|ctrl
        if 26.4 > i > 25.2:
            databit = black
#kanaly5-6
        if 28.4 > i > 26.4:
            databit = red|ctrl
        if 29.2 > i > 28.4:
            databit = black
        if 31.2 > i > 29.2:
            databit = red|ctrl
        if 32.4 > i > 31.2:
            databit = black
#kanaly7-8
        if 34.4 > i > 32.4:
            databit = red|ctrl
        if 35.2 > i > 34.4:
            databit = black
        if 37.2 > i > 35.2:
            databit = red|ctrl
        if 38.4 > i > 37.2:
            databit = black
#kanaly9-10
        if 40.4 > i > 38.4:
            databit = red|ctrl
        if 41.2 > i > 40.4:
            databit = black
        if 43.2 > i > 41.2:
            databit = red|ctrl
        if 44.4 > i > 43.2:
            databit = black
#kanaly11-12
        if 46.4 > i > 44.4:
            databit = red|ctrl
        if 47.2 > i > 46.4:
            databit = black
        if 49.2 > i > 47.2:
            databit = red|ctrl
        if 50.4 > i > 49.2:
            databit = black  
#kanaly13-14
        if 52.4 > i > 50.4:
            databit = red|ctrl
        if 53.2 > i > 52.4:
            databit = black
        if 55.2 > i > 53.2:
            databit = red|ctrl
        if 56.4 > i > 55.2:
            databit = black
#kanaly15-16
        if 58.4 > i > 56.4:
            databit = red|ctrl
        if 59.2 > i > 58.4:
            databit = black
        if 61.2 > i > 59.2:
            databit = red|ctrl 
        if i > 61.2:
            databit = black
        databit2 = databit|fh2

        f.write(databit2.to_bytes(1, byteorder='big'))
def stroka_signala_yellow_chet():
    for i in np.arange(period, hmicros, period):
        databit2 = 0
        if 0<i < c+period:
            databit = black 

        if c < i < y+period:
            databit = sync

        if y < i < cbstart+period:
            databit = black

        if cbstart < i < cbstop+period:    
            databit = cb

        if cbstop < i < b+period:
            databit = black
#kanaly1-2
        if 14.4 > i > b:
            databit = black
        if 16.4 > i > 14.4:
            databit = yellow|ctrl
        if 17.2 > i > 16.4:
            databit = black
        if 19.2 > i > 17.2:
            databit = yellow|ctrl
        if 20.4 > i > 19.2:
            databit = black
#kanaly3-4
        if 22.4 > i > 20.4:
            databit = yellow|ctrl
        if 23.2 > i > 22.4:
            databit = black
        if 25.2 > i > 23.2:
            databit = yellow|ctrl
        if 26.4 > i > 25.2:
            databit = black
#kanaly5-6
        if 28.4 > i > 26.4:
            databit = yellow|ctrl
        if 29.2 > i > 28.4:
            databit = black
        if 31.2 > i > 29.2:
            databit = yellow|ctrl
        if 32.4 > i > 31.2:
            databit = black
#kanaly7-8
        if 34.4 > i > 32.4:
            databit = yellow|ctrl
        if 35.2 > i > 34.4:
            databit = black
        if 37.2 > i > 35.2:
            databit = yellow|ctrl
        if 38.4 > i > 37.2:
            databit = black
#kanaly9-10
        if 40.4 > i > 38.4:
            databit = yellow|ctrl
        if 41.2 > i > 40.4:
            databit = black
        if 43.2 > i > 41.2:
            databit = yellow|ctrl
        if 44.4 > i > 43.2:
            databit = black
#kanaly11-12
        if 46.4 > i > 44.4:
            databit = yellow|ctrl
        if 47.2 > i > 46.4:
            databit = black
        if 49.2 > i > 47.2:
            databit = yellow|ctrl
        if 50.4 > i > 49.2:
            databit = black  
#kanaly13-14
        if 52.4 > i > 50.4:
            databit = yellow|ctrl
        if 53.2 > i > 52.4:
            databit = black
        if 55.2 > i > 53.2:
            databit = yellow|ctrl
        if 56.4 > i > 55.2:
            databit = black
#kanaly15-16
        if 58.4 > i > 56.4:
            databit = yellow|ctrl
        if 59.2 > i > 58.4:
            databit = black
        if 61.2 > i > 59.2:
            databit = yellow|ctrl 
        if i > 61.2:
            databit = black
          
        databit2 = databit
        f.write(databit2.to_bytes(1, byteorder='big'))

def stroka_signala_yellow_nechet():
    for i in np.arange(period, hmicros, period):
        databit2 = 0
        if 0<i < c+period:
           databit = black

        if c < i < y+period:
           databit = sync

        if  y < i < cbstart+period:
            databit = black

        if  cbstart < i < cbstop+period:    
            databit = cb
            
        if cbstop < i < b+period:
            databit = black
#kanaly1-2
        if 14.4 > i > b:
            databit = black
        if 16.4 > i > 14.4:
            databit = yellow|ctrl
        if 17.2 > i > 16.4:
            databit = black
        if 19.2 > i > 17.2:
            databit = yellow|ctrl
        if 20.4 > i > 19.2:
            databit = black
#kanaly3-4
        if 22.4 > i > 20.4:
            databit = yellow|ctrl
        if 23.2 > i > 22.4:
            databit = black
        if 25.2 > i > 23.2:
            databit = yellow|ctrl
        if 26.4 > i > 25.2:
            databit = black
#kanaly5-6
        if 28.4 > i > 26.4:
            databit = yellow|ctrl
        if 29.2 > i > 28.4:
            databit = black
        if 31.2 > i > 29.2:
            databit = yellow|ctrl
        if 32.4 > i > 31.2:
            databit = black
#kanaly7-8
        if 34.4 > i > 32.4:
            databit = yellow|ctrl
        if 35.2 > i > 34.4:
            databit = black
        if 37.2 > i > 35.2:
            databit = yellow|ctrl
        if 38.4 > i > 37.2:
            databit = black
#kanaly9-10
        if 40.4 > i > 38.4:
            databit = yellow|ctrl
        if 41.2 > i > 40.4:
            databit = black
        if 43.2 > i > 41.2:
            databit = yellow|ctrl
        if 44.4 > i > 43.2:
            databit = black
#kanaly11-12
        if 46.4 > i > 44.4:
            databit = yellow|ctrl
        if 47.2 > i > 46.4:
            databit = black
        if 49.2 > i > 47.2:
            databit = yellow|ctrl
        if 50.4 > i > 49.2:
            databit = black  
#kanaly13-14
        if 52.4 > i > 50.4:
            databit = yellow|ctrl
        if 53.2 > i > 52.4:
            databit = black
        if 55.2 > i > 53.2:
            databit = yellow|ctrl
        if 56.4 > i > 55.2:
            databit = black
#kanaly15-16
        if 58.4 > i > 56.4:
            databit = yellow|ctrl
        if 59.2 > i > 58.4:
            databit = black
        if 61.2 > i > 59.2:
            databit = yellow|ctrl 
        if i > 61.2:
            databit = black
        databit2 = databit|fh2

        f.write(databit2.to_bytes(1, byteorder='big'))
        
def stroka_signala_green_chet():
    for i in np.arange(period, hmicros, period):
        databit2 = 0
        if 0<i < c+period:
            databit = black 

        if c < i < y+period:
            databit = sync

        if y < i < cbstart+period:
            databit = black

        if cbstart < i < cbstop+period:    
            databit = cb

        if cbstop < i < b+period:
            databit = black
#kanaly1-2
        if 14.4 > i > b:
            databit = black
        if 16.4 > i > 14.4:
            databit = green|ctrl
        if 17.2 > i > 16.4:
            databit = black
        if 19.2 > i > 17.2:
            databit = green|ctrl
        if 20.4 > i > 19.2:
            databit = black
#kanaly3-4
        if 22.4 > i > 20.4:
            databit = green|ctrl
        if 23.2 > i > 22.4:
            databit = black
        if 25.2 > i > 23.2:
            databit = green|ctrl
        if 26.4 > i > 25.2:
            databit = black
#kanaly5-6
        if 28.4 > i > 26.4:
            databit = green|ctrl
        if 29.2 > i > 28.4:
            databit = black
        if 31.2 > i > 29.2:
            databit = green|ctrl
        if 32.4 > i > 31.2:
            databit = black
#kanaly7-8
        if 34.4 > i > 32.4:
            databit = green|ctrl
        if 35.2 > i > 34.4:
            databit = black
        if 37.2 > i > 35.2:
            databit = green|ctrl
        if 38.4 > i > 37.2:
            databit = black
#kanaly9-10
        if 40.4 > i > 38.4:
            databit = green|ctrl
        if 41.2 > i > 40.4:
            databit = black
        if 43.2 > i > 41.2:
            databit = green|ctrl
        if 44.4 > i > 43.2:
            databit = black
#kanaly11-12
        if 46.4 > i > 44.4:
            databit = green|ctrl
        if 47.2 > i > 46.4:
            databit = black
        if 49.2 > i > 47.2:
            databit = green|ctrl
        if 50.4 > i > 49.2:
            databit = black  
#kanaly13-14
        if 52.4 > i > 50.4:
            databit = green|ctrl
        if 53.2 > i > 52.4:
            databit = black
        if 55.2 > i > 53.2:
            databit = green|ctrl
        if 56.4 > i > 55.2:
            databit = black
#kanaly15-16
        if 58.4 > i > 56.4:
            databit = green|ctrl
        if 59.2 > i > 58.4:
            databit = black
        if 61.2 > i > 59.2:
            databit = green|ctrl 
        if i > 61.2:
            databit = black
          
        databit2 = databit
        f.write(databit2.to_bytes(1, byteorder='big'))

def stroka_signala_green_nechet():
    for i in np.arange(period, hmicros, period):
        databit2 = 0
        if 0<i < c+period:
           databit = black

        if c < i < y+period:
           databit = sync

        if  y < i < cbstart+period:
            databit = black

        if  cbstart < i < cbstop+period:    
            databit = cb
            
        if cbstop < i < b+period:
            databit = black
#kanaly1-2
        if 14.4 > i > b:
            databit = black
        if 16.4 > i > 14.4:
            databit = green|ctrl
        if 17.2 > i > 16.4:
            databit = black
        if 19.2 > i > 17.2:
            databit = green|ctrl
        if 20.4 > i > 19.2:
            databit = black
#kanaly3-4
        if 22.4 > i > 20.4:
            databit = green|ctrl
        if 23.2 > i > 22.4:
            databit = black
        if 25.2 > i > 23.2:
            databit = green|ctrl
        if 26.4 > i > 25.2:
            databit = black
#kanaly5-6
        if 28.4 > i > 26.4:
            databit = green|ctrl
        if 29.2 > i > 28.4:
            databit = black
        if 31.2 > i > 29.2:
            databit = green|ctrl
        if 32.4 > i > 31.2:
            databit = black
#kanaly7-8
        if 34.4 > i > 32.4:
            databit = green|ctrl
        if 35.2 > i > 34.4:
            databit = black
        if 37.2 > i > 35.2:
            databit = green|ctrl
        if 38.4 > i > 37.2:
            databit = black
#kanaly9-10
        if 40.4 > i > 38.4:
            databit = green|ctrl
        if 41.2 > i > 40.4:
            databit = black
        if 43.2 > i > 41.2:
            databit = green|ctrl
        if 44.4 > i > 43.2:
            databit = black
#kanaly11-12
        if 46.4 > i > 44.4:
            databit = green|ctrl
        if 47.2 > i > 46.4:
            databit = black
        if 49.2 > i > 47.2:
            databit = green|ctrl
        if 50.4 > i > 49.2:
            databit = black  
#kanaly13-14
        if 52.4 > i > 50.4:
            databit = green|ctrl
        if 53.2 > i > 52.4:
            databit = black
        if 55.2 > i > 53.2:
            databit = green|ctrl
        if 56.4 > i > 55.2:
            databit = black
#kanaly15-16
        if 58.4 > i > 56.4:
            databit = green|ctrl
        if 59.2 > i > 58.4:
            databit = black
        if 61.2 > i > 59.2:
            databit = green|ctrl 
        if i > 61.2:
            databit = black
        databit2 = databit|fh2

        f.write(databit2.to_bytes(1, byteorder='big'))
                

def stroki1_2():
    for t in np.arange(0, hmicros, period):
        if t < 27.3+period:
            databit = sync

        if 27.3 < t < 32+period:
            databit = black

        if 32 < t < 59.3+period:
            databit = sync

        if t > 59.3:
            databit = black

        f.write(databit.to_bytes(1, byteorder='big'))


def stroka3():
    for j in np.arange(0, hmicros, period):
        if j < 27.3:
            databit = sync
        if 27.3 < j < 32:
            databit = black
        if 32 < j < 35.35:
            databit = sync
        if j > 35.35:
            databit = black
        f.write(databit.to_bytes(1, byteorder='big'))


def stroka4_5():
    for l in np.arange(0, hmicros, period):
        if l < z:
            databit = sync

        if z < l < 32:
            databit = black

        if 32 < l < 34.35:
            databit = sync

        if l > 34.35:
            databit = black

        f.write(databit.to_bytes(1, byteorder='big'))

def stroka6_24_chet():
    for m in np.arange(0, hmicros, period):
        databit = 0
        if m < c:
            databit = black
         
        if c < m < y:
            databit = sync

        if cbstart+period > m > y:
            databit = black
 
        if cbstart < m < cbstop:
            databit = cb

        if cbstop < m:
            databit = black
        databit2 = databit
        f.write(databit2.to_bytes(1, byteorder='big'))
             
def stroka6_24_nechet():
    for m in np.arange(0, hmicros, period):
        databit = 0
        if m < c:
            databit = black
         
        if c < m < y+period:
            databit = sync

        if cbstart+period > m > y:
            databit = black
 
        if cbstart < m < cbstop+period:
            databit = cb

        if cbstop < m:
            databit = black

        databit2 = databit|fh2

        f.write(databit2.to_bytes(1, byteorder='big'))
def stroka311_312():
    for o in np.arange(0, hmicros, period):
        if o < z+period:
            databit = sync
        if z < o < 32+period:
            databit = black

        if 32 < o < 34.35+period:
            databit = sync

        if o > 34.35:
            databit = black
        f.write(databit.to_bytes(1, byteorder='big'))

def stroka313():
    for p in np.arange(0, hmicros, period):
        if p < z+period:
            databit = sync

        if z < p < 32+period:
            databit = black

        if 32 < p < 59.3+period:
            databit = sync

        if p > 59.3:
            databit = black

        f.write(databit.to_bytes(1, byteorder='big'))

def stroki314_315():
    for r in np.arange(0, hmicros, period):
        if r < 27.3+period:
            databit = sync

        if 27.3 < r < 32+period:
            databit = black

        if 32 < r < 59.3+period:
            databit = sync

        if r > 59.3:
            databit = black

        f.write(databit.to_bytes(1, byteorder='big'))

def stroka316_317():
    for s in np.arange(0, hmicros, period):
        if s < z+period:
            databit = sync

        if z < s < 32+period:
            databit = black

        if 32 < s < 34.35+period:
            databit = sync

        if s > 34.35:
            databit = black

        f.write(databit.to_bytes(1, byteorder='big'))

def stroka318():
    for u in np.arange(0, hmicros, period):
        if u < z+period:
            databit = sync

        if u > z:
            databit = black

        f.write(databit.to_bytes(1, byteorder='big'))

def stroka319_336_nechet():
    for x in np.arange(0, hmicros, period):
        databit2 = 0
        if x < c+period:
            databit = black
        
        if c < x < y+period:
            databit = sync

        if cbstart+period > x > y:
            databit = black
 
        if cbstart < x < cbstop+period:    
            databit = cb

        if cbstop < x:
            databit = black
        
        databit2 = databit|fh2
        f.write(databit2.to_bytes(1, byteorder='big'))

def stroka319_336_chet():
    for x in np.arange(0, hmicros, period):
        databit2 = 0
        if x < c+period:
            databit = black
        
        if c < x < y+period:
            databit = sync

        if cbstart+period > x > y:
            databit = black
 
        if cbstart < x < cbstop+period:    
            databit = cb
        if cbstop < x:
            databit = black

        databit2 = databit
        f.write(databit2.to_bytes(1, byteorder='big'))

def stroka623():
    for n in np.arange(0, hmicros, period):
        if n < c+period:
            databit = black
        if c < n < y+period:
            databit = sync

        if y < n < 32+period:
            databit = black

        if 32 < n < 34.35+period:
            databit = sync

        if n > 34.35:
            databit = black

        f.write(databit.to_bytes(1, byteorder='big'))

def stroka624():
    for v in np.arange(0, hmicros, period):
        if v < z+period:
            databit = sync

        if z < v < 32+period:
            databit = black

        if 32 < v < 34.35+period:
            databit = sync

        if v > 34.35:
            databit = black
        f.write(databit.to_bytes(1, byteorder='big'))
def stroka625():
    for q in np.arange(0, 59, period):
        if q < z+period:
            databit = sync

        if z < q < 32+period:
            databit = black

        if 32 < q < 34.35+period:
            databit = sync

        if 58.8 > q > 34.35:
            databit = black
        if q == 58.9:
            databit = reset
        f.write(databit.to_bytes(1, byteorder='big'))
        

while g < a+1:
    if 0< g < 3:
        stroki1_2()

        print('stroki1_2')
    if g == 3:
        stroka3()

        print('stroka3')
    if 3 < g < 6:
        stroka4_5()

        print('stroka4_5')
    if 5 < g < 25:
        if g % 2 == 0:
            stroka6_24_chet()
        else:
            stroka6_24_nechet()     
        print('stroka6_24')
    if 24 < g < 41: 
        if g % 2 == 0:
            stroka_signala_16_chet()
        else:
            stroka_signala_16_nechet()
#VHODY     
    if 40 < g < 57: 
        if g % 2 == 0:
            stroka_signala_red_chet()
        else:
            stroka_signala_red_nechet()
    if 56 < g < 65: 
        if g % 2 == 0:
            stroka_signala_yellow_chet()
        else:
            stroka_signala_yellow_nechet()
    if 64 < g < 169: 
        if g % 2 == 0:
            stroka_signala_green_chet()
        else:
            stroka_signala_green_nechet()
            
    if 168 < g < 177: 
        if g % 2 == 0:
            stroka_signala_8_chet()
        else:
            stroka_signala_8_nechet()
#VYHODY     
    if 176 < g < 193: 
        if g % 2 == 0:
            stroka_signala_red_chet()
        else:
            stroka_signala_red_nechet()
    if 192 < g < 201: 
        if g % 2 == 0:
            stroka_signala_yellow_chet()
        else:
            stroka_signala_yellow_nechet()
    if 200 < g < 305: 
        if g % 2 == 0:
            stroka_signala_green_chet()
        else:
            stroka_signala_green_nechet()
    if 304 < g < 311: 
        if g % 2 == 0:
            stroka_signala_8_chet()
        else:
            stroka_signala_8_nechet()
            
    if 310 < g < 313:
        stroka311_312()
        print('stroka311_312')
    if g == 313:
        stroka313()
        print('stroka313')
    if 313 < g < 316:
        stroki314_315()
        print('stroki314_315')
    if 315 < g < 318:
        stroka316_317()
        print('stroka316_317')
    if g == 318:
        stroka318()
        print('stroka318')
    if 318 < g < 336:
        if g % 2 == 0:
            stroka319_336_chet()
        else:
             stroka319_336_nechet()
        print('stroki319_336')
        
    if 335 < g < 352:
        if g % 2 == 0:
             stroka_signala_16_chet()          
        else:
             stroka_signala_16_nechet()
    if 351 < g < 368:
        if g % 2 == 0:
             stroka_signala_red_chet()          
        else:
             stroka_signala_red_nechet()
    if 367 < g < 376:
        if g % 2 == 0:
             stroka_signala_yellow_chet()          
        else:
             stroka_signala_yellow_nechet()
    if 375 < g < 480:
        if g % 2 == 0:
             stroka_signala_green_chet()          
        else:
             stroka_signala_green_nechet()
       
    if 479 < g < 488:
        if g % 2 == 0:
             stroka_signala_8_chet()          
        else:
             stroka_signala_8_nechet()
#VYHODY 
    if 487 < g < 504:
        if g % 2 == 0:
             stroka_signala_red_chet()          
        else:
             stroka_signala_red_nechet()
    if 503 < g < 512:
        if g % 2 == 0:
             stroka_signala_yellow_chet()          
        else:
             stroka_signala_yellow_nechet()
    if 511 < g < 616:
        if g % 2 == 0:
             stroka_signala_green_chet()          
        else:
             stroka_signala_green_nechet()
    if 615 < g < 623:
        if g % 2 == 0:
             stroka_signala_8_chet()          
        else:
             stroka_signala_8_nechet()    
    if g == 623:
        stroka623()
        print('stroka623')
    if g == 624:
        stroka624()
        print('stroka624')
    if g == 625:
        stroka625()
        print('stroka625')
    print(g)
    g += 1

f.close()
