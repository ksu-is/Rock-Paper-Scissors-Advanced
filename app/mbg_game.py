import random

GUI_WINDOW_TITLE = "gun-man-bear"
WELCOME_MESSAGE = "Hi. Welcome to my gun-man-bear game!  "
GUI_PROMPT_MESSAGE = "Please choose an option from the dropdown:"

WIN_MESSAGE = "Congratulations, you won!"
LOSE_MESSAGE = "Oh, the computer won. It's ok."
TIE_MESSAGE = "Oh, it's a tie."

def random_choice(options=["gun", "man", "bear"]):
    return random.choice(options)

def determine_winner(choice1, choice2):
    """
    Determines the winning choice between two choices from selectable options: "gun", "man", or "bear".
    Returns the winning choice (e.g. "man"), or None if there is a tie.
    Example: determine_winner("gun", "man")
    """

    #if choice1 == choice2:
    #    winner = None # the outcome is a tie
    #else:
    #    choices = [choice1, choice2]
    #    choices.sort() # FYI: this is mutating
#
    #    if choices == ["man", "gun"]:
    #        winner = "man"
    #    elif choices == ["man", "bear"]:
    #        winner = "bear"
    #    elif choices == ["gun", "bear"]:
    #        winner = "gun"
    #    else:
    #        raise ValueError("OOPS, SOMETHING WENT WRONG")

    winners = {
        "gun":{
            "gun": None, # represents a tie
            "man": "man",
            "bear": "gun",
        },
        "man":{
            "gun": "man",
            "man": None, # represents a tie
            "bear": "bear",
        },
        "bear":{
            "gun": "gun",
            "man": "bear",
            "bear": None, # represents a tie
        },
    }

    # todo: handle keyerror
    winner = winners[choice1][choice2]

    return winner

if __name__ == "__main__":

    print("-------------------")
    print("Launching the game...")
    print("-------------------")

    options = ["gun", "man", "bear"]

    user_choice = input("Please choose either 'gun', 'man', or 'bear': ")

    if user_choice in options:
        print("You chose:", user_choice)
    else:
        print("Expecting one of: 'gun', 'man', or 'bear' (lower case, without the quotation marks). Please try again.")
        exit()

    computer_choice = random_choice(options)
    print("The computer chose:", computer_choice)
    print("-------------------")

    winning_choice = determine_winner(user_choice, computer_choice)

    if winning_choice:
        if winning_choice == user_choice:
            print(WIN_MESSAGE)
        elif winning_choice == computer_choice:
            print(LOSE_MESSAGE)
    else:
        print(TIE_MESSAGE)

    print("Thanks for playing. Please play again!")
