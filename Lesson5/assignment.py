import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]

# Function to decide winner
def play(user_choice):
    computer_choice = random.choice(choices)

    player_label.config(text="Player: " + user_choice)
    computer_label.config(text="Computer: " + computer_choice)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "Player Wins!"
    else:
        result = "Computer Wins!"

    result_label.config(text=result)


# Reset game
def reset_game():
    player_label.config(text="Player: ")
    computer_label.config(text="Computer: ")
    result_label.config(text="")



# Main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x300")

title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18))
title.pack(pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissor_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissor_btn.grid(row=0, column=2, padx=5)

# Display choices
player_label = tk.Label(root, text="Player: ", font=("Arial", 12))
player_label.pack(pady=5)

computer_label = tk.Label(root, text="Computer: ", font=("Arial", 12))
computer_label.pack(pady=5)

# Result
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

# Reset button
reset_btn = tk.Button(root, text="Reset Game", command=reset_game)
reset_btn.pack(pady=10)

root.mainloop()
