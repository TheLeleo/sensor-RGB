from machine import I2C, Pin
import utime
from sensorConfig import *

# Configuração da comunicação I2C
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)

# Configuração inicial do sensor
configure_sensor(i2c)

# Loop principal
while True:
    clear, vermelho, verde, azul = read_color_values(i2c)
    
    media = (vermelho + verde + azul)/3
    
    r = (vermelho/media)*100
    g = (verde/media)*100
    b = (azul/media)*100
    print('R',r,'G',g,'B',b)
    
    utime.sleep(1)



