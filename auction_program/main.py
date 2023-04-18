# secret auction program

import os
from functions import *
from data import auction_data

os.system("clear")
# simple greet
greet()

while True:
    # we ask for a name and bid
    if in_name_and_bid():
        break

# who's the winner
winner()
