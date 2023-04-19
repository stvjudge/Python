from data import data
import art

import os
import random


def out_logo():
    print(art.logo)


def rand_from_dict():
    return random.choice(data)


def higher_or_lower(value: str, vs1: dict, vs2: dict):
    if vs1["follower_count"] > vs2["follower_count"] and value == "a":
        return vs1
    if (
        vs1["follower_count"] < vs2["follower_count"]
        and value == "a"
        or vs1["follower_count"] > vs2["follower_count"]
        and value == "b"
    ):
        return 0
    if vs1["follower_count"] < vs2["follower_count"] and value == "b":
        return vs2


def vs(point, vs1: dict):
    os.system("cls" if os.name == "nt" else "clear")
    out_logo()
    # dictionary
    if point == 0:
        vs1 = rand_from_dict()
    vs2 = rand_from_dict()
    # print("vs1: ", vs1)
    # print("vs2: ", vs2)
    # print("point: ", point)
    if vs1 == vs2:
        vs()
    print("You're right! Current score: ", point) if (point > 0) else None
    print(f"Compare A: {vs1['name']}, {vs1['description']} from {vs1['country']}")
    print(art.vs)
    print(f"Compare B: {vs2['name']}, {vs2['description']} from {vs2['country']}")
    a_b = higher_or_lower(
        input("Who has more followers? Type 'A' or 'B': ").lower(), vs1, vs2
    )
    if a_b == 0:
        print("You lost, your score is ", point)
        return
    else:
        print(a_b)
        point += 1
        vs(point, a_b)
