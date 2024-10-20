# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=("yes", "no")):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # Check if the user response is a word in the list
            if item == user_response:
                return item

            # Check of the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # Print error if user does not enter something that is valid
        print(error)
        print()


# Displays instructions
def instruction():
    print('''

**** Instructions ****

To begin, choose the number of rounds (or press <enter> for infinite mode).

Then play against the computer. You need to choose R (rock), P (paper), S (scissors).

The rules are as follows:
o Paper beats rock
o Rock beats scissors
o Scissors beats paper

Press <xxx> to end the game at anytime

Good luck

    ''')


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

rps_list = ["rock", "paper", "scissors", "xxx"]


print("💎📃✂️Rock/Paper/Scissors Game💎📃✂️")
print()

# Ask user if they want to see the instructions and display
want_instructions = string_checker("Do you want to read the instructions?")

# Checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

# Ask user for number of rounds/infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5
    
# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings (based on mode)
    if mode == "infinite":
        rounds_heading = f"\nRound {rounds_played + 1} (Infinite Mode) "
    else:
        rounds_heading = f"\nRound {rounds_played + 1} of {num_rounds}"

    print(rounds_heading)
    print()

    # Get user choice
    user_choice = string_checker("Choose: ", rps_list)
    print("You chose", user_choice)

    # If user choice is the exit code, break the loop
    if user_choice == "xxx":
        break

    rounds_played += 1

    # If users are in infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1

# Game loop ends here

# Game history/statistics area
