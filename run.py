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

# Function to get user confirmation before starting the game
def ask_ready():
    while True:
        ready = input("Type 'yes' to start or 'no' to exit: \n").strip().lower()
        if ready == 'yes':
            return True
        elif ready == 'no':
            print("Exiting the game. See you next time!")
            return False
        else:
            print("Invalid input. Please type 'yes' to start or 'no' to exit.\n")

# Create board
def create_board():
    return [["~"] * Board_size for _ in range(Board_size)]

# Print board
def print_board(board):
    # Add column headers (A-E)
    print("  " + " ".join(chr(65 + i) for i in range(Board_size)))
    for i, row in enumerate(board):
        # Add row numbers (1-5) on the left side
        print(f"{i+1} " + " ".join(row))
    print() # Print a newline after the board

# Function to randomly place the ship
def place_ship():
    ship_row = random.randint(0, Board_size - 1)
    ship_col = random.randint(0, Board_size - 1)
    return (ship_row, ship_col)

# Place multiple ships
def place_ships():
    ships = []
    while len(ships) < Num_ships:
        ship_row, ship_col = place_ship()
        if (ship_row, ship_col) not in ships:  # Ensure no duplicate ships
            ships.append((ship_row, ship_col))
    return ships

