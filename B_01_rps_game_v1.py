# Check that users have entered a valid
# option based on a list
def int_check(question):

    while True:
        error = "Please enter an integer that is 1 or more"

        to_check = input(question)

        # Check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # Checks that the number is more than/equal to 1
            if response < 1:
                print(error)

            else:
                return response

        except ValueError:
            print(error)


# Main Routine

# Intialise game variables
mode = "regular"
rounds_played = 0

print("💎📃✂️Rock/Paper/Scissors Game💎📃✂️")
print()

# Instructions

# Ask user for number of rounds/infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    print("You chose infinite")
    num_rounds = 5
    
# Game loop starts here
while rounds_played < num_rounds:
    user_choice = input("Choose: ")
    # Ends infinite loop
    if user_choice == "xxx":
        break

    rounds_played += 1
    print("Rounds played: ", rounds_played)

    # If users are in infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1

    print("Num rounds: ", num_rounds)
# Game loop ends here

# Game history/statistics area
