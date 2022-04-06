"""LU base component - based on 00_LU_base_v1
Components added after they have been created and tested
"""
import random


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


# Function to generate random token
def generate_token(balance):

    rounds_played = 0
    play_again = ""

    # Testing loop to generate 5 tokens
    while play_again != "x":
        rounds_played += 1  # keep track of rounds
        number = random.randint(1, 100)  # can only be a donkey

        # adjust balance
        # If the random number is between 1 and 5
        # user gets a unicorn (add $4 to balance)
        if 1 <= number <= 5:
            token = "unicorn"
            balance += 4
            print(formatter("!", "Congratulations, you got a unicorn"))
            print()

        # if the random number is between 6 and 36
        # user gets a donkey (subtract $1 from balance)
        elif 6 <= number <= 36:
            token = "donkey"
            balance -= 1

        # in all other cases the token must be a horse or a zebra
        # (subtract $0.50 from the balance in either case)
        else:
            # if the number is even, set the token to zebra
            if number % 2 == 0:
                token = "zebra"
                balance -= 0.50

            # otherwise, set the token to horse
            else:
                token = "horse"
                balance -= 0.50

        # output
        print(f"Round {rounds_played}. Token: {token}. Balance: ${balance}:.2f")
        if balance < 1:
            print("\nSorry but you have run out of money")
            play_again = "x"
        else:
            play_again = input("\nDo you want to play another round?\n<enter> to play again or 'X' to quit").lower()
        print()
    return balance


# function to format text output
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom} \n{formatted_text}\n{top_bottom}"


# Main routine go here...
print(formatter("-", "Welcome to the Lucky Unicorn Game"))
print()
played_before = yes_no("Have you played the game before (Y for yes/N for No): ")

if played_before == "No":
    instructions()


# ask the user how much they want to play with
starting_balance = num_check("How much would you like to play with? $", 1, 10)
print(f"You are playing with ${starting_balance}")

closing_balance = generate_token(starting_balance)
print("Thanks for playing")
print(f"Starting balance = ${starting_balance:.2f}")
print(f"Final balance = ${closing_balance:.2f}")
print()
print(formatter("*", "Goodbye"))
