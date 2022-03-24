# Ask the user if the have played before
instruction_check = input("Have you played the game before (Y for yes/N for No):").upper

# If they say yes, output 'Program Continues'
if instruction_check == "Y":
    print("Program Continues")

# If they say no, output 'Display Instructions'
elif instruction_check == "N":
    print("Display Instructions")

# Otherwise - show error
else:
    print("Please enter either Y/N.")
