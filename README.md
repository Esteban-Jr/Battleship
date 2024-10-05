# Battleships

"Battleships" is a timeless strategy game in which players strive to sink their opponent's ships. In this iteration, you will face off against a computer adversary on a 5x5 grid, tasked with locating and destroying all enemy vessels concealed on the board.

The live link can be found here - [Battleships](https://battleships-vs-computer-d6d3e8954180.herokuapp.com/)

![Battleship Am I Responsive Image](/assets/images/responsive.png)

## User Experience (UX) & Design

For this project, the user interface is crafted to be intuitive and engaging, despite the limitations of a command-line format. The aim is to deliver a visually appealing experience through effective text formatting. Important information is centered on the screen for prominence, while text effects are used sparingly to enhance readability without distracting the user.

To achieve a refined look, spaces and line breaks are strategically positioned to highlight key messages and actions. This method fosters a clean and organized layout, directing the user's focus to essential elements of the game, including instructions, prompts, and results.

### User Stories

As a player, I want the game to provide the following features:

- List of instructions
- A board that shows my guesses and where I can guess
- Know whether my guess is a hit or miss
- A turn counter to let me know which turn I am on

### Gameplay

When the game starts, the instructions are displayed in the terminal, followed by the board. This board shows the positions of all previous shots, and any hits on enemy ships will be marked.

- The player is prompted to enter a row number between 1 and 5 for their shot
 - If the guess is not within the range, the player will be prompted to enter a valid row number once more
- The player is then asked to enter a column letter between A and E
 - If the guess is not letter between A and E, the player will be asked again for a valid column letter
- After each guess, the player will be let known if it was a "Hit" or a "Miss"
- The player will be let known before each guess which turn they are on
- The game will continue until the player runs out of turns or the player has "Hit" all the ships
- At the end a message will be displayed indicating the end of the game, this message will either say "Game over! You've run out of turns." or "Congratulations! You've sunk all the ships!"

