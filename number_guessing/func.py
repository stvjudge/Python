import random
import os


def greet():
    os.system("clear")
    print(
        """
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
    """
    )


y_win = 1, "You Win!"
t_low = 2, "Too low!"
t_high = 3, "Too High!"
y_lost = 4, "You Lost!"


def choose_difficulty():
    return (
        5 if input("  Choose a difficulty. Type 'easy' or 'hard': ") == "hard" else 10
    )


def check_number(my_number, number_to_guess):
    if my_number == number_to_guess:
        return y_win
    if my_number < number_to_guess:
        return t_low
    if my_number > number_to_guess:
        return t_high


def play_game(attempts):
    os.system("clear")
    number_to_guess = random.randint(1, 101)
    tipp: int = 0
    while tipp != number_to_guess:
        print("Attempts left: ", attempts)
        tipp = int(input("Make a guess: "))
        result = check_number(tipp, number_to_guess)
        if result[0] == 1:
            print(y_win[1])
            break
        match result[0]:
            case 2:
                print(t_low[1])
            case 3:
                print(t_high[1])
        if 0 == attempts - 1:
            print(y_lost[1])
            break
        attempts -= 1
        print("-----------------------")


def end():
    if input("(e)xit?: ") == "e":
        return True
    return False
