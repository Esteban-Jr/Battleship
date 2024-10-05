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


# Get player's guess (with input validation)
def get_player_guess(board):
    while True:
        try:
            # Ask for the row as a number between 1 and 5
            guess_row = input(f"Guess Row (1-{Board_size}): ")
            
            # Check if the input is an integer and within the correct range
            if guess_row.isdigit():
                guess_row = int(guess_row)
                if 1 <= guess_row <= Board_size:
                    guess_row -= 1  # Convert to zero-indexed system
                else:
                    print(f"Invalid row! Please enter a number between 1 and {Board_size}.")
                    continue  # Ask for input again
            else:
                print("Invalid input! Please enter a number.")
                continue

            # Ask for the column as a letter between A and E
            guess_col = input(f"Guess Column (A-{chr(65 + Board_size - 1)}): ").upper()

            # Check if the column is a letter within the allowed range
            if len(guess_col) == 1 and 'A' <= guess_col <= chr(65 + Board_size - 1):
                guess_col = ord(guess_col) - 65  # Convert 'A' to 0, 'B' to 1, etc.
            else:
                print(f"Invalid column! Please enter a letter between A and {chr(65 + Board_size - 1)}.")
                continue  # Ask for input again

            # Check if the guess has already been made or is a valid spot
            if board[guess_row][guess_col] in ["O", "X"]:
                print("You've already guessed that coordinate. Please try again.")
                continue  # Ask for input again
            
            # Return the validated and converted guess
            return (guess_row, guess_col)
        
        except ValueError:
            print("Invalid input! Please enter a valid row number.")

