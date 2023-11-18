from machine import I2C, Pin
import utime
from sensorConfig import *

# comunicação I2C
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)

# Configurar sensor i2c
configure_sensor(i2c)

# loop de execução do programa
while True:
    clear, vermelho, verde, azul = read_color_values(i2c)
    
    media = (vermelho + verde + azul)/3
    
    r = (vermelho/media)*100
    g = (verde/media)*100
    b = (azul/media)*100
    print('R',r,'G',g,'B',b)
    
    utime.sleep(1)