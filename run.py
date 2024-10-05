import random

# Constants for board size
Board_size = 5

# Number of ships and turns
Num_ships = 5
Max_turns = 15

# Function to display the game instructions
def display_instructions():
    print("Welcome to the Battleships Game!")
    print("Instructions:")
    print(f"- The game is played on a {Board_size}x{Board_size} grid.")
    print(f"- There are {Num_ships} hidden ships randomly placed on the grid.")
    print("- Your task is to guess their positions and sink them.")
    print("- The rows are numbered 1 to 5 and the columns are labeled A to E.")
    print("- You have 10 turns to sink all the ships.")
    print("- A 'Hit' is marked with an 'X', and a 'Miss' is marked with an 'O'.\n")
    print("Are you ready to start the game? (yes/no)\n")

