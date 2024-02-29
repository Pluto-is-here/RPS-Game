def int_checker(question):
    while True:
        error = "Please enter an integer that is 1 or more"

        to_check = input(question
                         )
        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # Checks that the number is more than / equal to 1

            if response < 1:
                print(error)

            else:
                return response

        except ValueError:
            print(error)


# check the users have entered a
# valid option based on a list

def string_checker(question, valid_ans=("yes", "no")):
    error = f"Please enter a valid option from the following list {valid_ans}"

    while True:

        # get user_response and make sure it's lowercase

        user_response = input(question).lower()

        for item in valid_ans:
            # Check if the user response is a word in the list
            if item == user_response:
                return item

            # Check if the user response is the same as the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid

        print(error)
        print()


def instructions():
    print(''' 

    *** Instructions ***

    To begin, choose the number of rounds, or play on infinite mode.

    Then play against the computer. You need to choose R (rock), P (paper) or S (scissors)

    The rules are as follows:

    - Paper beats rock
    - Rock beats scissors
    - Scissors beats paper

    Good luck!
    ''')


# main routine starts here

# initialise game variables
mode = "regular"
rounds_played = 0

rps_list = ["rock", "paper", "scissors", "xxx"]

print(" 💎📰✂ Rock/Paper/Scissors Game 💎📰✂")
print()

# Instructions
want_instructions = string_checker("Do you want to view instructions? ")

if want_instructions == "yes":
    instructions()


# Ask users for number of rounds / infinite mode
num_rounds = int_checker("How many rounds would you like? Push <enter> for infinite mode: ")
print()

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings:
    if mode == "infinite":
        rounds_heading = f"\n ♾♾♾ Round {rounds_played + 1} (Infinite mode) ♾♾♾"
    else:
        rounds_heading = f"\n 🕰🕰🕰 Round {rounds_played} (Regular mode) 🕰🕰🕰 "

    print(rounds_heading)
    print()

    # get user choice
    user_choice = string_checker("Choose: ", rps_list)
    print("you chose", user_choice)

    # if user choice is exit code, break the loop

    if user_choice == "xxx":
        break

    rounds_played += 1

    # If users chose infinite, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

# Game loop ends here

# Game stats
