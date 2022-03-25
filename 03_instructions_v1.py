"""Took function from component 03_v1 as the basis for this new function
which incorporates both yes/no and show instructions"""


# Function goes here...
def yes_no(question_text):
    while True:

        # Ask the user if the have played before
        answer = input(question_text).upper()

        # If they say yes, output 'Program Continues'
        if answer == "Y" or answer == "YES":
            answer = "Yes"
            return answer

        # If they say no, output 'Display Instructions'
        elif answer == "N" or answer == "NO":
            answer = "No"
            return answer

        # Otherwise - show error
        else:
            print("Please enter either Y/N or Yes/No")

# Function to display instructions
def instructions():
    print("*** How to Play ***")
    print()
    print("The rules of the game will go here")
    print()
    print("Program continues")
    print()


# Main routine go here...
played_before = yes_no("Have you played the game before (Y for yes/N for No): ")

if played_before == "No":
    instructions()
else:
    print("Program continues")
