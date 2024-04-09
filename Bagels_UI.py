import random
import tkinter as tk
from tkinter import messagebox


# Function to handle the guess button click
def guess_number():
    global number_of_guess
    global secret_number

    guess = guess_entry.get()
    if not guess.isdigit() or len(guess) != 3:
        messagebox.showerror("Error", "Please enter a 3-digit number.")
        return

    guess_number = [int(char) for char in guess]
    numbers_intersect = list(set(secret_number) & set(guess_number))

    if guess_number == secret_number:
        messagebox.showinfo("Congratulations!", "You guessed the correct number!")
        reset_game()
    elif not numbers_intersect:
        result_label.config(text="Bagels")
    else:
        result = ""
        for j in range(len(guess_number)):
            if guess_number[j] == secret_number[j]:
                result += "Fermi "
            elif guess_number[j] in secret_number:
                result += "Pico "
        result_label.config(text=result)

    guess_history_text.insert(tk.END,
                              f"Guess #{number_of_guess}: {guess}\n{'Bagels' if not numbers_intersect else result}\n\n")
    guess_history_text.see(tk.END)  # Scroll the text widget to the bottom

    number_of_guess += 1
    if number_of_guess > max_guesses:
        messagebox.showinfo("Game Over",
                            "Sorry! You used all your chances to guess the correct number.\nThe secret number is: {}.".format(
                                ''.join(map(str, secret_number))))
        reset_game()

    guess_entry.delete(0, tk.END)  # Clear the entry box after a guess


# Function to reset the game
def reset_game():
    global secret_number
    secret_number = [random.randint(0, 9) for _ in range(3)]
    global number_of_guess
    number_of_guess = 1
    result_label.config(text="")
    guess_entry.delete(0, tk.END)


# Initialize the tkinter window
root = tk.Tk()
root.title("Number Guessing Game")

# Global variables
secret_number = [random.randint(0, 9) for _ in range(3)]
max_guesses = 10
number_of_guess = 1

# UI elements
intro_label = tk.Label(root, text="I am thinking of a 3-digit number. Try to guess what it is :).", justify=tk.LEFT)
intro_label.pack()

tk.Label(root, text="Here are some clues:", justify=tk.LEFT).pack()

clues_label = tk.Label(root,
                       text="When I say:       That means:\n           Pico           The digit is correct but in the wrong position\n           Fermi          The digit is correct and in the right position\n           Bagels        No digit is correct",
                       justify=tk.LEFT)
clues_label.pack()

tk.Label(root, text="Ok, I have thought up a number.", justify=tk.LEFT).pack()
tk.Label(root, text="You have 10 times to guess the correct number. Good luck :)", justify=tk.LEFT).pack()
tk.Label(root, text="", justify=tk.LEFT).pack()

tk.Label(root, text="Enter your guess (3 digits):", justify=tk.LEFT).pack()
guess_entry = tk.Entry(root)
guess_entry.pack()
tk.Button(root, text="Guess", command=guess_number).pack()

result_label = tk.Label(root, text="", justify=tk.LEFT)
result_label.pack()

guess_history_text = tk.Text(root, height=10, width=50)
guess_history_text.pack()

# Start the tkinter event loop
root.mainloop()
