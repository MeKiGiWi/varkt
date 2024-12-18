"""drawing graphics using data.json and our_data.json"""
from json import load
import matplotlib.pyplot as plt


def main():
    plt.ylabel('Gravity force')
    plt.xlabel('Time')
    plt.grid(True)
    with open('data.json', 'r', encoding='UTF-8') as f:
        database = load(f)
        plt.plot([x[0] for x in database], [x[1] for x in database])
    # cur_time, acceleration, speed, height, temperature, atm_pressure, env_density, env_resistance_force, mass * g
    with open('our_data.json', 'r', encoding='UTF-8') as f:
        database = load(f)
        plt.plot([x[0] for x in database], [x[3] for x in database], color='r')
    plt.show()


if __name__ == "__main__":
    main()