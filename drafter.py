import matplotlib.pyplot as plt
from json import load 


def main():
    plt.ylabel('Gravity force')
    plt.xlabel('Time')
    plt.grid(True)
    with open('data.json', 'r') as f:
        database = load(f)
        plt.plot([x[0] for x in database], [x[1] for x in database])
    # cur_time, acceleration, speed, height, temperature, atm_pressure, env_density, env_resistance_force, mass * g
    with open('our_data.json', 'r') as f:
        database = load(f)
        plt.plot([x[0] for x in database], [x[3] for x in database], color='r')
    plt.show()


if __name__ == "__main__":
    main()