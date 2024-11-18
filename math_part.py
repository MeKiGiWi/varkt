import scipy.constants as cons
import json
import math
from time import sleep


def temp_by_elev(height):
    # temperature depending by elevating
    if (0 <= height <= 3000):
        temperature = 288.2 - 3.2 * height * 1e-3
    elif (3000 <= height <= 11000):
        temperature = 268.7 - 6.5 * (height * 1e-3 - 3)
    elif (11000 <= height <= 20000):
        temperature = 216.7
    elif (20000 <= height <= 32000):
        temperature = 216.7 + (height * 1e-3 - 20)
    elif (32000 <= height <= 40000):
        temperature = 228.5 + 2.75 * (height * 1e-3 - 32)
    elif (40000 <= height <= 50000):
        temperature = 250.4 + 2 * (height * 1e-3 - 40)
    elif (50000 <= height <= 60000):
        temperature = 270.7 - 2.3 * (height * 1e-3 - 50)
    elif (60000 <= height <= 80000):
        temperature = 247 - 2.45 * (height * 1e-3 - 60)
    elif (80000 <= height <= 100_000):
        temperature = 198.6 - 0.1 * (height * 1e-3 - 80)
    elif (100_000 <= height <= 150_000):
        temperature = 196.6 + 8.62 * (height * 1e-3 - 100)
    else:
        temperature = 627.6
    return temperature


# cтартовые данные
height = 0
speed = 0
start_mass = 41_400
acceleration = 0
# константные данные
Cf = 0.42
push_force = 490_000
area = pow(1.95, 2) * cons.pi
nu = 0.029
parachutes_square_20000 = 3 * pow(0.65, 2) * cons.pi
parachutes_square_2000 = 3 * pow(1.95, 2) * cons.pi - parachutes_square_20000
atm_pressure_on_earth = 101_325
# вспомогательные переменные
database = []
parachutes_open_20000 = False
parachutes_open_2000 = False
engine_works = True
booster_detached = False
# a = (F тяги / m) - g - F сопрот
for i in range(1, int(10e4)):
    if (height <= 500 and not(engine_works)):
        break
    if (height >= 42400):
        engine_works = False
    k = 0.25
    cur_time = k * i # current second
    if (engine_works):
        mass = start_mass - cur_time * 228 # current mass
    g = cons.G * 5.9722 * 1e24 / pow(6378100 + height, 2) # current gravity acceleration 
    temperature = temp_by_elev(height)
    atm_pressure = atm_pressure_on_earth * math.exp(-nu * g * height / (cons.R * temperature)) # current atmosphere pressure 
    env_density = nu * atm_pressure / (cons.R * temperature)
    env_resistance_force = area * env_density * pow(speed, 2) * 0.5 * Cf
    if (engine_works):
        acceleration = (push_force / mass) - g - (env_resistance_force / mass)
    else:
        if speed > 0:
            acceleration = -g - (env_resistance_force / mass)
        else:
            acceleration = -g + (env_resistance_force / mass)
    speed += k * acceleration
    height += k * speed
    if (not(booster_detached) and height >= 106500 and speed <= 10):
        mass = 5500
        booster_detached = True
        Cf = 1.15
    # sleep(0.5)
    # print(cur_time, speed, acceleration, height)
    database.append([cur_time, speed, acceleration, height, temperature])
    if (not engine_works and height <= 20000 and not parachutes_open_20000):
        parachutes_open_20000 = True 
        area += parachutes_square_20000 * 1.136
    if (not engine_works and height <= 2000 and not parachutes_open_2000):
        parachutes_open_2000 = True 
        area += parachutes_square_2000 * 1.136
with open('our_data.json', 'w') as f:
    json.dump(database, f)
