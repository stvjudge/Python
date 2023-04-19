# number guessing game
import func

# global variable
is_end = False

while not is_end:
    func.greet()
    attempt = func.choose_difficulty()
    func.play_game(attempt)
    is_end = func.end()
