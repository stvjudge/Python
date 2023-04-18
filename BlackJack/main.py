import func

end = False
while not end:
    func.show_logo()
    func.deal_the_cards()
    func.print_cards()
    player_total = func.player_cards()
    computer_total = func.comp_cards()
    func.print_cards_final(player_total, computer_total)
    func.winner(player_total, computer_total)
    end = func.end()
