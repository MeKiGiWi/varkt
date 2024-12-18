"""calculating absolute and relative error"""
import json


def main():
    with open("our_data.json", "r", encoding="UTF-8") as f:
        max_height_in_our_model = 0
        time_of_max_height_inourmodel = 0
        height_on_375s = 0
        database = json.load(f)
        for step in database:
            if max_height_in_our_model < step[3]:
                max_height_in_our_model = step[3]
                time_of_max_height_inourmodel = step[0]

        for step in database:
            if step[0] == 375:
                height_on_375s = step[3]

    with open("data.json", "r", encoding="UTF-8") as f:
        database = json.load(f)
        for step in database:
            if step[0] >= time_of_max_height_inourmodel:
                print((max_height_in_our_model - step[1]) / 107500)
                print(max_height_in_our_model - step[1])
                break

        for step in database:
            if step[0] >= 375:
                print((step[1] - height_on_375s) / 107500)
                print(step[1] - height_on_375s)
                break


if __name__ == "__main__":
    main()