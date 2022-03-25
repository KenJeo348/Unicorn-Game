"""Component 2 (How much) v2
Use try/accept and pull error message out of the loop"""

error = "Please enter a whole number between 1 and 10\n"
user_balance = 0

# Keep asking until a valid amount (1-10) is entered
while not 1 <= user_balance <= 10:
    try:
        # ask for amount
        user_balance = int(input("Please enter a whole number between 1 and 10\n"
                                 "How much would you like to play with? $"))
        print()

    except ValueError:
        print(error)

print(f"You are playing with $P{user_balance}")
