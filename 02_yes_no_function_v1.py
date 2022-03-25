"""Yes/No checking function
based on 01_yes_no_v2
"""


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


# Main routine go here...
show_instructions = yes_no("Have you played the game before (Y for yes/N for No): ")
print(f"You entered {show_instructions}")
print()
having_fun = yes_no("Are you having fun? ")
print(f"You entered '{having_fun}'")
