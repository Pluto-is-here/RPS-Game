import random


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


# compares user and computer choice
def rps_compare(user, computer):
    if user == computer:
        result = "tie"

        return result

    elif user == "paper" and computer == "rock":
        result = "win"
        return result

    elif user == "rock" and computer == "scissors":
        result = "win"
        return result

    elif user == "scissors" and computer == "paper":
        result = "win"
        return result

    else:
        result = "lose"
        return result


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
rounds_won = 0
rounds_tied = 0
rounds_lost = 0

rps_list = ["rock", "paper", "scissors", "xxx"]
game_history = []

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

    # randomly choose from RPS list (excluding exit code)
    comp_choice = random.choice(rps_list[:-1])
    print(f"The computer chose {comp_choice}")

    round_result = rps_compare(user_choice, comp_choice)

    rounds_played += 1

    # adjust game lost/ game tied counters and add result to game history

    if round_result == "tie":
        feedback = "👔👔 It's a tie. 👔👔"
        rounds_tied += 1

    elif round_result == "lose":
        feedback = "😥😥 You lost... 😥😥"
        rounds_lost += 1

    else:
        feedback = "🎉🎉 You won! 🎉🎉"

    round_feedback = f"{user_choice} vs {comp_choice}... {feedback}"
    history_item = f'{rounds_played} - {round_feedback}'
    print(round_feedback)

    game_history.append(history_item)

    # If users chose infinite, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

# Game loop ends here

# Game stats
if rounds_played > 0:

    rounds_won = rounds_played - rounds_tied - rounds_lost
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100
    percent_tied = 100 - percent_won - percent_lost

    print("📊📊📊 Game Statistics 📊📊📊")
    print(f" Won: {percent_won:.2f}% \t"
          f" Lost: {percent_lost:.2f}% \t"
          f" Tied: {percent_tied:.2f}% ")

    print()

    want_stats = string_checker("Do you want to see game history? ")

    if want_stats == "yes":

        "⌛ Game History ⌛"

        for item in game_history:
            print(item)

    print()
    print("Thanks for playing!")

else:
    print("🐔🐔🐔 Oops - You chickened out! 🐔🐔🐔")

