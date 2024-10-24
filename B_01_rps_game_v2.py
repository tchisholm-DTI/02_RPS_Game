# Check that users have entered a valid
# option based on a list
import random


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


# Compares user/computer choice and returns
# result (win/lose/tie)
def rps_compare(user, comp):
    if user == comp:
        round_result = "tie"

    # There are three ways to win

    # If the user chooses paper and computer chooses rock, user wins
    elif user == "paper" and comp == "rock":
        round_result = "win"
    # If the user chooses rock and computer chooses scissors, user wins
    elif user == "scissors" and comp == "paper":
        round_result = "win"
    # If the user chooses scissors and computer chooses paper, user wins
    elif user == "rock" and comp == "scissors":
        round_result = "win"

    # If it's not a win/tie, then it's a loss
    else:
        round_result = "lose"

    return round_result


# Main Routine

# Intialise game variables
mode = "regular"
rounds_played = 0
rounds_tied = 0
rounds_lost = 0
# rounds_won = rounds_played - rounds_lost - rounds_tied (code for later)

rps_list = ["rock", "paper", "scissors", "xxx"]
game_history = []


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
        rounds_heading = f"\n💿💿 Round {rounds_played + 1} (Infinite Mode) 💿💿 "
    else:
        rounds_heading = f"\n💿💿 Round {rounds_played + 1} of {num_rounds} 💿💿"

    print(rounds_heading)
    print()

    # Randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(rps_list[:-1])
    print("Computer choice", comp_choice)

    # Get user choice
    user_choice = string_checker("Choose: ", rps_list)
    print("You chose", user_choice)

    # If user choice is the exit code, break the loop
    if user_choice == "xxx":
        break

    result = rps_compare(user_choice, comp_choice)

    # Adjust game lost/game tied counters and add results to game history
    if result == "tie":
        rounds_tied +=1
        feedback = "👔👔 It's a tie! 👔👔"
    elif result == "lose":
        rounds_lost +=1
        feedback = "😢😢 You lose. 😢😢"
    else:
        feedback = "👍👍 You won.👍👍"

    # Set up round feedback and output it - user
    # Add it to the game history list (include the round number)
    round_feedback = f"{user_choice} vs {comp_choice}, {feedback}"
    history_item = f"Round: {rounds_played} - {round_feedback}"

    print(round_feedback)
    game_history.append(history_item)

    rounds_played += 1

    # If users are in infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1

# Game loop ends here

# Game history/statistics area
if rounds_played > 0:

    # Calculate Statistics
    rounds_won = rounds_played - rounds_tied - rounds_lost
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100
    percent_tied = 100 - percent_won - percent_lost

    # Output Game Statistics
    print("📊📊📊 Game Statistics 📊📊📊")
    print(f"👍Won: {percent_won:.2f} \t " 
          f"😢Lost: {percent_lost:.2f} \t "
          f"👔Tied: {percent_tied:.2f}")

    # Ask user if they want to see their game history and output it if requested
    see_history = string_checker("\nDo you want to see your game history? ")
    if see_history == "yes":
        for item in game_history:
            print(item)

    print()
    print("Thanks for playing. ")

else:
    print("🐔🐔🐔 Oops - You chickened out! 🐔🐔🐔")
