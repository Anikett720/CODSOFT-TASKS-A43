import tkinter as tk
import random

# Initialize scores
user_score = 0
computer_score = 0

def determine_winner(user_choice, computer_choice):
    global user_score, computer_score
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        user_score += 1
        return "You win!"
    else:
        computer_score += 1
        return "Computer wins!"

def play_game(user_choice):
    computer_choice = random.randint(1, 3)
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

    # Update scores
    user_score_label.config(text=f"Your score: {user_score}")
    computer_score_label.config(text=f"Computer score: {computer_score}")

    # Show play again button
    play_again_button.pack(pady=5)

def on_play_button_click():
    user_choice = choice_var.get()
    play_game(user_choice)

def on_play_again_button_click():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_score_label.config(text=f"Your score: {user_score}")
    computer_score_label.config(text=f"Computer score: {computer_score}")
    result_label.config(text="")
    play_again_button.pack_forget()  # Hide play again button

# Create main window
root = tk.Tk()
root.title("CODSOFT - R.P.S - Game")

# Create choice variable
choice_var = tk.IntVar()

# Create choice frame
choice_frame = tk.Frame(root)
choice_frame.pack(pady=10)

# Create choice radio buttons
tk.Radiobutton(choice_frame, text="Rock", variable=choice_var, value=1).pack(side=tk.LEFT, padx=10)
tk.Radiobutton(choice_frame, text="Paper", variable=choice_var, value=2).pack(side=tk.LEFT, padx=10)
tk.Radiobutton(choice_frame, text="Scissors", variable=choice_var, value=3).pack(side=tk.LEFT, padx=10)

# Create play button
play_button = tk.Button(root, text="Play", command=on_play_button_click)
play_button.pack(pady=10)

# Create result label
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Create play again button
play_again_button = tk.Button(root, text="Play Again", command=on_play_again_button_click)

# Create score tracker labels
user_score_label = tk.Label(root, text="Your score: 0")
user_score_label.pack(pady=5)
computer_score_label = tk.Label(root, text="Computer score: 0")
computer_score_label.pack(pady=5)

# Run the application
root.mainloop()