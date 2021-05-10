from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox

from game import *

window = tkinter.Tk()

window.title(GUI_WINDOW_TITLE)

my_message = tkinter.Message(text=WELCOME_MESSAGE, width=1000)
my_select_label = tkinter.Label(text=GUI_PROMPT_MESSAGE)
def handle_button_click(c):
    user_choice = c
    computer_choice = random_choice()
    winning_choice = determine_winner(user_choice, computer_choice)

    message = "-------------------"
    message += f"\nYou chose: {user_choice}"
    message += f"\nThe computer chose: {computer_choice}"
    message += "\n-------------------"

    if winning_choice:
        if winning_choice == user_choice:
            message += f"\n{WIN_MESSAGE}"
        elif winning_choice == computer_choice:
            message += f"\n{LOSE_MESSAGE}"
    else:
        message += f"\n{TIE_MESSAGE}"

    message += "\n-------------------"
    message += "\nThanks for playing. Please play again!"

    tkinter.messagebox.showinfo("Results...", message)
def button_rock():
    click = "rock"
    handle_button_click(click)
def button_scissors():
    click = "scissors"
    handle_button_click(click)
def button_paper():
    click = "paper"
    handle_button_click(click)
rock = Button(window,text="rock",command=lambda:button_rock())
paper = Button(window,text="paper", command=lambda:button_paper())
scissors = Button(window,text="scissors", command=lambda:button_scissors())
my_message.pack()
my_select_label.pack()
rock.pack()
paper.pack()
scissors.pack()
window.mainloop()
