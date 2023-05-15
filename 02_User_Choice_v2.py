# Version 2 - error message included when calling function

# Functions go here
def choice_checker(question):

    valid = False
    while not valid:

        # Ask user for choice and check it's validr
        response = input(question).lower()

        if response == "r" or response == "rock":
            return "rock"
        elif response == "p" or response == "paper":
            return "paper"
        elif response == "s" or response == "scissors":
            return "scissors"

        # Check for exit code
        elif response == "xxx":
            return "xxx"

# Main routine goes here


# Loop for testing purposes
user_choice = ""
while user_choice != "xxx":

    # Ask user for choice and check it's valid
    user_choice = choice_checker("Choose rock/paper/scissors r/p/s", "Please choose from rock/paper/scissors" "(or xxx to quit")

    # Print out choice for comparison purposes
    print("You chose {}".format(user_choice))
