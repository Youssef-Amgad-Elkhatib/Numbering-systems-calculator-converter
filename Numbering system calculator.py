# Author: Youssef Amgad Abd Al Halim Ahmed
# Description :Calculator that converts any numbering system to the rest of the systems




def main():    # created main function which calls all functions #
    menu1()
    number = (input_number())
    choice_2 = menu2()
    choice_3 = menu3()
    # calling functions that we will use in the menus #

    ''' if conditions to see which choices user inputted 
    and accordingly send number to correct function to convert'''
    # checking validity of inserted number according to each system #
    if choice_3=="A" and choice_2=="A":
        for i in range(len(number)):
            if number[i] in ["0","1","2","3","4","5","6","7","8","9"]:
                continue
            else:
                print("The inserted number doesn't belong to this system")
                main() # returning to main function to repeat process if number is invalid in the first system #
        print(number)

    elif choice_3=="B" and choice_2=="B":
        for i in range(len(number)):
            if number[i] in ["0","1"]:
                continue
            else:
                print("The inserted number doesn't belong to this system")
                main()
        print(number)

    elif choice_3=="C" and choice_2=="C":
        for i in range(len(number)):
            if number[i] in ["0","1","2","3","4","5","6","7"]:
                continue
            else:
                print("The inserted number doesn't belong to this system")
                main()
        print(number)

    elif choice_3=="D" and choice_2=="D":
        for i in range(len(number)):
            if number[i] in ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]:
                continue
            else:
                print("The inserted number doesn't belong to this system")
                main()
        print(number)

    elif choice_2 in ["A"] and choice_3 in ["B"]:
        for i in range(len(number)):
            if number[i] in ["0","1","2","3","4","5","6","7","8","9"]:
                continue
            else:
                print("The inserted number doesn't belong to this system")
                main()
        number=int(number)
        print(dec_to_bin(number))

    elif choice_2 in ["A"] and choice_3 in ["C"]:
        for i in range(len(number)):
            if number[i] in ["0","1","2","3","4","5","6","7","8","9"]:
                continue
            else:
                print("The inserted number doesn't belong to this system")
                main()
        number=int(number)
        print(dec_to_octal(number))

    elif choice_2 in ["A"] and choice_3 in ["D"]:
        for i in range(len(number)):
            if number[i] in ["0","1","2","3","4","5","6","7","8","9"]:
                continue
            else:
                print("The inserted number doesn't belong to this system")
                main()
        number=int(number)
        value=dec_to_hexadecimal(number)
        print(value)


    elif choice_2 in ["B"] and choice_3 in ["A"]:
        for i in range(len(number)):
            if number[i] in ["0","1"]:
                continue
            else:
                print("The inserted number doesn't belong to this system")
                main()
        print(bin_to_dec(number))

    elif choice_2 in ["B"] and choice_3 in ["C"]:
        for i in range(len(number)):
            if number[i] in ["0","1"]:
                continue
            else:
                print("The inserted number doesn't belong to this system")
                main()
        bin_to_octal(number)

    elif choice_2 in ["B"] and choice_3 in ["D"]:
        for i in range(len(number)):
            if number[i] in ["0","1"]:
                continue
            else:
                print("The inserted number doesn't belong to this system")
                main()
        bin_to_hexadecimal(number)

    elif choice_2 in ["C"] and choice_3 in ["A"]:
        for i in range(len(number)):
            if number[i] in ["0","1","2","3","4","5","6","7"]:
                continue
            else:
                print("The inserted number doesn't belong to this system")
                main()
        print(octal_to_dec(number))

    elif choice_2 in ["C"] and choice_3 in ["B"]:
        for i in range(len(number)):
            if number[i] in ["0","1","2","3","4","5","6","7"]:
                continue
            else:
                print("The inserted number doesn't belong to this system")
                main()
        octal_to_bin(number)

    elif choice_2 in ["C"] and choice_3 in ["D"]:
        for i in range(len(number)):
            if number[i] in ["0","1","2","3","4","5","6","7"]:
                continue
            else:
                print("The inserted number doesn't belong to this system")
                main()
        octal_to_hex(number)

    elif choice_2 in ["D"] and choice_3 in ["A"]:
        for i in range(len(number)):
            if number[i] in ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]:
                continue
            else:
                print("The inserted number doesn't belong to this system")
                main()
        print(hex_to_dec(number))

    elif choice_2 in ["D"] and choice_3 in ["B"]:
        for i in range(len(number)):
            if number[i] in ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]:
                continue
            else:
                print("The inserted number doesn't belong to this system")
                main()
        hex_to_bin(number)

    elif choice_2 in ["D"] and choice_3 in ["C"]:
        for i in range(len(number)):
            if number[i] in ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]:
                continue
            else:
                print("The inserted number doesn't belong to this system")
                main()
        hex_to_octal(number)





    print()
    print()

    main() # calling main function(recursion) to restart process until user exits #


def menu1():       # created Menu1 as a function #
    # print Menu1 options#


    print("**numbering system converter**")
    print()
    print("A) insert a new number")
    print("B) exit")
    print()

    # taking choice from user #
    choice_1=input("Please enter A or B ")
    if choice_1 == "B":exit()            # if choice is B exit the system #



    elif choice_1 not in ["A","B"]:            # if choice is invalid recall function Menu1 from beginning #
        print("Please select a valid choice")
        print()
        menu1()
def input_number(): # choice_A function takes number from user and checks if it is a valid number #

    x = False # bool assigned to use in the while loop#
    num1 = input("Please insert a valid number ")# entered number in the form of string to check its validity #
    while not x:

        for i in range(len(num1)):# making sure that the entered number is valid in the four systems #
            if num1[i] not in ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]:
                x = False
                break
            else: x=True
        if x: break
        num1 = input("Please enter a valid number ")# if number isn't valid retake input from user #



    return num1 # return value of num1 #



def menu2(): # menu2 function choosing which system to convert from #
    # printing menu2 options #

    print("**Please select the base you want to convert a number from**")
    print("A) Decimal")
    print("B) Binary")
    print("C) Octal")
    print("D) Hexadecimal")
    print()
    choice_2=input("Please select A or B or C or D ")
    x = True # bool to test validity of while loop #
    while x:
        if choice_2 in ["A","B","C","D"]:# checking if choice_2 is valid #
            x=False

        else:
            print("Please enter a valid choice")# if not retake choice from user #
            choice_2 = input()
            x=True
    return choice_2 # return value of the choice to use in the if conditions in main function #







def menu3():  # menu3 function displays systems to concert to #
    print("**Please select the base you want to convert a number to**")
    print("A) Decimal")
    print("B) Binary")
    print("C) Octal")
    print("D) Hexadecimal")
    print()
    x=True # bool to test validity of while loop #
    choice_3 = input("Please select A or B or C or D ")
    while x:

        if choice_3 in ["A","B","C","D"]:  # checking if choice_3 is valid #
            x=False

        else:
            print("Please enter a valid choice ")  # if not valid retake choice from user #
            choice_3 = input()
            x=True
    return choice_3 # returning value of choice #


def dec_to_bin(number): # function to convert from decimal to binary #
    place_holder = ""  # place_holder string to hold integer of decimal number #
    while number >= 1:
        remainder = number / 2  # dividing by 2 #
        remainder = remainder % 1  # getting decimal part of the number #
        dec = str(int((remainder * 2)))  # multiplying decimal part by 2 to get decimal value and converting to string to hold value #

        place_holder = place_holder+dec  # concatenation of place_holder with string value of decimal #

        number = number // 2  # integer division of original number to repeat loop with an integer not float value #
    reversed_place_holder = place_holder[::-1]  # reversing placeholder to return correct sequence #
    return reversed_place_holder



def dec_to_octal(number):
    place_holder = ""  # place_holder string to hold integer of octal number #
    while number >= 1:

        remainder = number / 8  # dividing by 8 #
        remainder = remainder % 1  # getting decimal part of the number #
        octal = str(int((remainder * 8)))  # multiplying decimal part by 8 to get octal value and converting to string to hold value #


        place_holder = place_holder+octal  # concatenation of place_holder with string value of octal #

        number = number // 8  # integer division of original number to repeat loop with an integer not float value #
    reversed_place_holder = place_holder[::-1]  # reversing placeholder to return correct sequence #
    return reversed_place_holder






def dec_to_hexadecimal(number):
    place_holder = "" # place_holder string to hold integer of hexadecimal number #
    while number>=1:

        remainder = number / 16 # dividing by 16 #
        remainder=remainder % 1 # getting decimal part of the number #
        hexa = str(int((remainder * 16))) # multiplying decimal part by 16 to get hexadecimal value and converting to string to hold value and convert to letters of hexadecimal system if needed #
        if hexa=="10": hexa="A" # converting to letter form if needed #
        if hexa=="11": hexa="B"
        if hexa=="12": hexa="C"
        if hexa=="13": hexa="D"
        if hexa=="14": hexa="E"
        if hexa=="15": hexa="F"

        place_holder=place_holder+hexa # concatenation of place_holder with string value of hexadecimal #


        number=number//16 # integer division of original number to repeat loop with an integer not float value #
    reversed_place_holder = place_holder[::-1] # reversing placeholder to return correct sequence #
    return reversed_place_holder


# noinspection PyShadowingBuiltins
def bin_to_dec(number):

    holder = "" # place holder string #
    for i in number: # for loop on indexes of number #
        holder = i + holder # concatenation of index of number in reverse from on placeholder #
    sum1=0 # decimal number value #
    power=0 # power of base 2 #
    for i in range(0,len(holder)):
        sum1 = sum1 + (2**power)*int(holder[i]) # calculating decimal from binary (known calculation) #
        power=power+1 # incrementation of power as we move along index of string #

    return sum1 # returning sum to print in main function #


def bin_to_octal(number):
    print((dec_to_octal(bin_to_dec(number)))) # using decimal as a bridge between binary and octal #

def bin_to_hexadecimal(number):
    print(dec_to_hexadecimal(bin_to_dec(number))) # using decimal as a bridge between binary and hexadecimal #

def octal_to_dec(number): # same idea as bin to dec but with base 8 instead of 2 #
    holder= ""
    for i in number:
        holder = i + holder
    sum1 = 0
    power = 0
    for i in range(0, len(holder)):
        sum1 = sum1 + (8 ** power) * int(holder[i])
        power = power + 1

    return sum1

def octal_to_bin(number): # decimal as a bridge between octal and binary #
    print(dec_to_bin(octal_to_dec(number)))

def octal_to_hex(number): # decimal as a bridge between octal and hexadecimal #
    print(dec_to_hexadecimal(octal_to_dec(number)))

def hex_to_dec(number): # same idea as any system to decimal #

    holder = ""
    my_dict={"A":10,"B":11,"C":12,"D":13,"E":14,"F":15} # dictionary to switch letter form with its corresponding number from #
    for i in number:
        holder = i + holder
    sum1 = 0
    power = 0
    for i in holder:
        if i.isalpha(): # function that detects if index i is one of hexadecimal letters #
            sum1 = sum1 + my_dict[i]*(16**power) # replacing letter with number form and multiplying by 16**n #
        else:
            sum1 = sum1 + (16 ** power) * int(i) # summing by multiplying number by 16**n #
        power = power + 1

    return sum1
def hex_to_bin(number):
    print(dec_to_bin(hex_to_dec(number))) # using decimal as a bridge between hex and binary #

def hex_to_octal(number):
    print(dec_to_octal(hex_to_dec(number))) # using decimal as a bridge between hex and octal #




main()   # calling main at the end to make sure interpreter read all previous functions #