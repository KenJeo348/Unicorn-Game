# Temporary While loop used for testing convenience.

instruction_check = ""
while instruction_check != "x":
    # Ask the user if the have played before
    instruction_check = input("Have you played the game before (Y for yes/N for No): ").upper()

    # If they say yes, output 'Program Continues'
    if instruction_check == "Y" or instruction_check == "YES":
        print("Program Continues")

    # If they say no, output 'Display Instructions'
    elif instruction_check == "N" or instruction_check == "NO":
        print("Display Instructions")

    # Otherwise - show error
    else:
        print("Please enter either Y/N.")
