import scipy.constants as cons
import json
import math
from time import sleep


# cтартовые данные
height = 0
speed = 0
start_temperature = 298.15
start_mass = 41_420
acceleration = 0
# константные данные
push_force = 490_000
area = pow(1.85, 2) * cons.pi
nu = 0.029
parachutes_square_20000 = 3 * pow(1.3, 2) * cons.pi
parachutes_square_10000 = 3 * pow(7.7, 2) * cons.pi
atm_pressure_on_earth = 101_325
# вспомогательные переменные
database = []
engine_works = True
booster_detached = False
parachutes_open_20000 = False
parachutes_open_10000 = False
# a = (F тяги / m) - g - F сопрот
for i in range(1, int(10e4)):
    if (height <= 100 and not(engine_works)):
        break
    if (height >= 42400):
        engine_works = False
    k = 0.25
    cur_time = k * i # current second
    if (engine_works):
        mass = start_mass - cur_time * 340.142 # current mass
    g = cons.G * 5.9722 * 1e24 / pow(6378100 + height, 2) # current gravity acceleration 
    temperature = start_temperature - 6 * height # current temperature
    atm_pressure = atm_pressure_on_earth / math.exp(nu * g * height / (cons.R * temperature)) # current atmosphere pressure 
    env_density = nu * atm_pressure / (cons.R * temperature)
    env_resistance_force = area * env_density * pow(speed, 2) / 4
    if (engine_works):
        acceleration = (push_force / mass) - g - (env_resistance_force / mass)
    else:
        acceleration = -g - (env_resistance_force / mass)
    speed += k * acceleration
    height += k * speed
    if (not(booster_detached) and height >= 106500):
        mass = 6000
        booster_detached = True
    if (height <= 20000 and not(parachutes_open_20000) and booster_detached):
        area += parachutes_square_20000
        parachutes_open_20000 = True
    elif (height <= 2500 and not(parachutes_open_10000) and booster_detached):
        area += parachutes_square_10000 - parachutes_square_20000
        parachutes_open_10000 = True
    # sleep(0.5)
    # print(cur_time, speed, acceleration, height)
    database.append([cur_time, height])

with open('our_data.json', 'w') as f:
    json.dump(database, f)
