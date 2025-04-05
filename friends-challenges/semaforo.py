import time
import os

semaforo = ['Verde', 'Amarelo', 'Vermelho']

os.system("clear")

time.time()
print('Estado do semáforo:', semaforo[2])

time.sleep(5)
print('Estado do semáforo:', semaforo[1])

time.sleep(2)
print('Estado do semáforo:', semaforo[0])

time.sleep(5)
print('Estado do semáforo:', semaforo[2])