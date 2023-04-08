import os
import requests
import random

name_list = []
device_list = [
    "Iphone 6",
    "Iphone 7",
    "Iphone 8",
    "Iphone 9",
    "Iphone 10",
    "Iphone 11",
    "Iphone 12",
    "Iphone 13",
    "Iphone 14",
    "Iphone 15",
    "Chromebook",
    "Samsung Galaxy S8",
    "Samsung Galaxy S9",
    "Samsung Galaxy S10",
    "Samsung Galaxy S11",
    "Samsung Galaxy S12",
    "Samsung Galaxy S13",
    "Samsung Galaxy S14",
    "Samsung Galaxy S15",
    "MacBook Air",
    "MacBook Pro",
    "IPad",
    "Ipad Pro",
    "Ipad Air",
    "Ipad Mini",
    "Huawei P40",
    "Huawei P50",
    "Huawei P60",
    "Huawei P70",
    "Huawei P80",
    "Huawei P90",
    "Xiaomi Mi 8",
    "Xiaomi Mi 9",
    "Xiaomi Mi 10",
    "Xiaomi Mi 11",
    "Xiaomi Mi 12",
    "Xiaomi Mi 13",
]


def get_names():
    response = requests.get("https://raw.githubusercontent.com/dominictarr/random-name/master/first-names.txt",
                            timeout=5).text
    with open("names.txt", "w") as f:
        for line in response.split("\n"):
            f.write(line + "\n")


def main():
    try:
        with open("names.txt") as f:
            for line in f:
                name_list.append(line.strip())

        random.shuffle(name_list)
        random.shuffle(device_list)

        rand_identity = f"{random.choice(name_list)}s {random.choice(device_list)}"
        os.system(f"hostnamectl set-hostname {str(rand_identity)}")
    except FileNotFoundError:
        get_names()
        main()


if __name__ == '__main__':
    main()
