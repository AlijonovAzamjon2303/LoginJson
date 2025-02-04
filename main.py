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

u = User("A", 1111)
u2 = User("B", 1111)
u3 = User("C", 1234)
lst = [u, u2, u3]


menu = ("1. Kirish"
        "2. Ro'yxat o'tish")

while True:
    print(menu)
    choice = input()
