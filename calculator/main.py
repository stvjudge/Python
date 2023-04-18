import func
import os

menu = 1

while menu:
    if menu == 1:
        os.system("clear")
        # print logo
        func.logo_draw()
        # we ask for a number input an we save it to var in_data
        func.in_number()
        # we ask the user witch operation want to use
    func.in_operation()
    # ask for number two
    func.in_number_two()
    # we make the calculation
    func.calculation()
    # print the calculation
    func.pri_calculation()

    menu = func.what_next()
