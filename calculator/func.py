import data
import art


def logo_draw():
    print(art.logo)


def in_number():
    data.in_data = float(input("What's the first number?: "))


def in_operation():
    data.in_symbol = input("*\n-\n+\n/\nPick an operation: ")


def in_number_two():
    data.in_data_two = float(input("What's the next number?: "))


def calculation():
    match data.in_symbol:
        case '+':
            data.outcome = data.in_data + data.in_data_two
        case '-':
            data.outcome = data.in_data - data.in_data_two
        case '/':
            data.outcome = data.in_data / data.in_data_two
        case '*':
            data.outcome = data.in_data * data.in_data_two


def pri_calculation():
    print(f"{data.in_data} {data.in_symbol} {data.in_data_two} = {data.outcome}")


def what_next():
    # continue calculate with the actual output
    match input(f"Type 'y' to continue calculating with {data.outcome} or type 'n' to start a new calculation or 'exit' to close the program: ").lower():
        case 'y':
            data.in_data = data.outcome
            return 2
        case 'n':
            return 1
        case 'exit':
            return 0
