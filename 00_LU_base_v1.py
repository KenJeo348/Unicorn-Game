"""LU base component
Components added after they have been created and tested"""


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


# number checking function
def num_check(question, low, high):
    error = "That was not valid input\n" \
            "Please enter a number between {} and {}\n".format(low, high)

    # Keep asking until a valid amount (1-10) is entered
    while True:
        try:
            # ask for amount
            response = int(input(question))

            # check for number within the required range
            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine go here...
played_before = yes_no("Have you played the game before (Y for yes/N for No): ")

if played_before == "No":
    instructions()


# ask the user how much they want to play with
user_balance = num_check("How much would you like to play with? $", 1, 10)
print(f"You are playing with ${user_balance}")

