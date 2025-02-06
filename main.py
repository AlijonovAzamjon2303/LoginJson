import json
from random import choice

from Models import User

path = "data.json"

def write(data):
    data = [x.to_dict() for x in data]

    with open(path, "w") as file:
        json.dump(data, file, indent=4)

def read():
    with open(path, "r") as file:
        data = json.load(file)
    data = [User.dict_to(d) for d in data]

    return data


menu = ("1. Kirish\n"
        "2. Ro'yxat o'tish")

while True:
    print(menu)
    choice = input(">>> ")
    if choice == "1":
        name = input("name = ")
        password = int(input("password = "))
        data = read()
        bormi = False
        for user in data:
            if user.name == name and user.password == password:
                bormi = True
                break
        if bormi:
            print("Xush kelibsiz", name)
        else:
            print("Sizga kirish mumkin emas!")
