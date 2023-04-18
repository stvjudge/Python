from data import *
from image import logo
import os


def greet():
    print(logo)
    print("Welcome to the Secret Auction program!")


def others():
    if input("Are there any other bidders? Type 'yes' or 'no'.\n") == 'yes':
        # clear screen
        os.system("clear")
        return 0
    else:
        return 1


def in_name_and_bid():
    name = input("What is your name?: ")
    return in_bid(name)


def in_bid(in_name):
    bid = float(input("What is your bid?: €"))
    auction_data[in_name] = bid
    return others()


def winner():
    os.system("clear")
    win_tup = calc_win()
    print(f"The winner is {win_tup[0]} with a bid of €{win_tup[1]}")


def calc_win():
    win_tup = ("", 0)
    for name, value in auction_data.items():
        if value > win_tup[1]:
            win_tup = name, value
    return win_tup
