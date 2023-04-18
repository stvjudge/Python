import data
import art
import random
import os


def show_logo():
    os.system("clear")
    print(art.logo)


def deal_the_cards():
    # null cards
    data.my_cards = []
    data.computer_cards = []
    # generate cards
    for i in range(2):
        data.my_cards.append(random.choice(list(data.cards.keys())))
        data.computer_cards.append(random.choice(list(data.cards.keys())))
    # print cards


def print_cards():
    print("Your cards: ", data.my_cards)
    print("Computer's first card: ", data.computer_cards[0])


def print_cards_final(total_player, total_computer):
    show_logo()
    print("***********************")
    print(f"Player's final hand: {data.my_cards} -> {total_player}")
    print(f"Computer's final hand: {data.computer_cards} -> {total_computer}")
    print("***********************")


def player_won():
    print("Player win!")


def computer_won():
    print("Computer win!")


def draw():
    print("Draw!")


def winner(total_player, total_computer):
    if total_player > 21 or total_computer < 22 and total_computer > total_player:
        computer_won()
    if (
        total_player < 22
        and total_player > total_computer
        or total_player < 22
        and total_computer > 21
    ):
        player_won()
    if total_player < 21 and total_player == total_computer:
        draw()


def player_cards():
    aces = 0
    for card in data.my_cards:
        if card == "A":
            aces += 1
    total = count_cards(data.my_cards)
    print_total(data.my_cards, aces)
    # ask for more
    want_new = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    while want_new == "y":
        show_logo()
        new_card = random.choice(list(data.cards.keys()))
        if new_card == "A":
            aces += 1
        data.my_cards.append(new_card)
        total += data.cards[new_card]
        print(f"Your cards: {data.my_cards} -> {total}")
        print_total(data.my_cards, aces)
        want_new = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if aces:
        for i in range(aces):
            if input("What value you want for 'A'(1/11)?: ") == "1":
                total -= 10
    # print(f"Your total: {total}")
    return total


def count_cards(cards: list):
    total = 0
    for card in cards:
        if type(card) == str:
            if card == "A":
                total += 11
            else:
                total += 10
        else:
            total += data.cards[card]
    return total


def print_total(cards: list, aces: int):
    total = count_cards(cards)
    if aces == 0:
        print(f"Your total: {total}")
        return
    print(f"Your total: {total}")
    for i in range(aces):
        print(f"Your total can also be: {total - (i + 1) * 10}")


def comp_cards():
    total = count_cards(data.computer_cards)
    if total >= 17:
        return total
    while total < 17:
        new_card = random.choice(list(data.cards.keys()))
        if new_card == "A" and total + data.cards[new_card] > 21:
            total += 1
        else:
            total += data.cards[new_card]
        data.computer_cards.append(new_card)
    return total


def end():
    is_end = input("Do you want to play again(y/n)?: ")
    if is_end == "y":
        return False
    else:
        return True
