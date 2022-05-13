import string
import random

ascii = list(string.ascii_letters)

digits = list(string.digits)

special = list("!@#$%^&*()")

def generate_random_password():

    finalnumber = abs(int(input("Type the max number of your password: ")))

    asciinumber = abs(int(input("type the number of letters: ")))

    digitsnumber = abs(int(input("Type the number of digits: ")))

    specialnumber = abs(int(input("Type the number of special characters you want: ")))

    password = []

    while finalnumber < asciinumber + digitsnumber + specialnumber:
        print("The max number is less than the lenght of ascii, digits and special, type again")
        finalnumber = abs(int(input("Type the max number of your password: ")))

        asciinumber = abs(int(input("type the number of letters: ")))

        digitsnumber = abs(int(input("Type the number of digits: ")))

        specialnumber = abs(int(input("Type the number of special characters you want: ")))
    
    random.shuffle(ascii)
    random.shuffle(digits)
    random.shuffle(special)

    for i in range(0,asciinumber):
        password.append(random.choice(ascii))
    
    for i in range(0,digitsnumber):
        password.append(random.choice(digits))
    
    for i in range(0,specialnumber):
        password.append(random.choice(special))

    random.shuffle(password)

    print("".join(password))
    password = "".join(password)
    upper = False

    for i in range(0,len(password)):
        if password[i].isupper() == True:
            upper = True

    
    while upper == False: 
        choose = input("It seems that your password does not have any upper letter, some sites may no accept it, do you want to try again? press 1 for yes anything for no: ")
        if  choose == "1":
            password = list(password)
            password = password.clear()
            password = []

            for i in range(0,asciinumber):
                password.append(random.choice(ascii))
    
            for i in range(0,digitsnumber):
                password.append(random.choice(digits))
    
            for i in range(0,specialnumber):
                password.append(random.choice(special))

            random.shuffle(password)

            print("".join(password))
            password = "".join(password)

            for i in range(0,len(password)):
                if password[i].isupper() == True:
                    upper = True
        else: 
            return
    
            

generate_random_password()

k = input("Press any key to leave")
	
