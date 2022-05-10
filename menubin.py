
def dec_bin():

    choice = "Y"
    while choice == "Y":
        decimal = int(input("Type a decimal number "))
        print("The number: " , decimal , "in binary is: " , bin(decimal)[2:])
        choice = input("Want to continue? press Y, if not press any other key ").upper()
        if choice != "Y":
            break

def bin_dec():
    choice = "Y"
    while choice == "Y":
        binary = input("Type a binary number ")
        print("The binary number: ", binary, "in decimal is: ", int(binary, 2))
        choice = input("Want to continue? press Y, if not press any other key ").upper()
        if choice != "Y":
            break

while True:
    menu_choice = int(input("1 - Convert decimal to binary\n2 - Convert binary to decimal\n3 - Exit the program\n"))
    if menu_choice == 1:
        dec_bin()
    elif menu_choice == 2:
        bin_dec()
    elif menu_choice == 3:
        quit()

    

