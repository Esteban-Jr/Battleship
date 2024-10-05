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

## Features

- Ships are placed randomly on the board at the start of each new game, guaranteeing a distinct experience with every session
- Player input is verified to confirm that all coordinates fall within the limits of the game board.
- The game restricts the player from targeting the same location multiple times.

## Software Used

Below is a list of the software/applications used in the construction of this project:

- [GitHub](https://github.com/)
    - Used to store and manage the project's code.
- [Visual Studio Code](https://code.visualstudio.com/)
    - Used as the project's Integrated Development Environment (IDE).
- [Heroku](https://dashboard.heroku.com/apps)
    - Used to deploy the application and host it online.
- [Am I Responsive](https://ui.dev/amiresponsive)
    - Used to create an image of the various display sizes of the site.

## Testing

## Game Testing

![Screenshot of starting page](/assets/images/starting_page.png)

When you run the program, you will be greeted with a "Welcome to the Battleships game !". This will be displayed at the top of the terminal

The is set in a 5x5 grid that act as the ocean, there are 5 ships, each will be a in a 1x1 cell. Your objective will be to find and destroy the 5 ships within 15 shots

The game's coordinate system is simple and easy to follow:

- Rows are numbered 1 to 5
- Columns are labeled A to E
- To make a guess, you will be asked for a row number followed by a column letter (e.g., 1 A), this system enables you to aim at precise grid locations for your shots.

![Are you ready?](/assets/images/start_game.png)

### User Input: Are you ready to start the game?

Before the game begins, you'll be asked a question: "Are you ready to start the game?". You have to respond "yes" or "no":

- If you type "yes," the game will start, and you'll move to the gameplay screen where you can begin guessing the positions of the enemy ships
- If you type "no", the system will display "Exiting the game. See you next time!" and the game will end

### Handling Invalid Inputs

If you enter anything other than "yes" or "no," the system will display a message indicating the input is invalid ("Invalid input. Please type 'yes' to start or 'no' to exit."). It will then repeatedly prompt you with "Type 'yes' to start or 'no' to exit:" until a valid response is given. This ensures the game begins only when the player is fully prepared and understands the rules.

![Invalid input](/assets/images/invalid_input.png)

During gameplay, you'll be prompted to enter the coordinates for your shot in an attempt to hit an enemy ship. The input process is simple, but it’s crucial to provide valid coordinates:

![Invalid coordinates](/assets/images/invalid_coordinates.png)

### Entering Coordinates

- Row Number: You must enter a row number between 1 and 5
- Column Letter: You must enter a column letter between A and E

### What Happens When You Get a Hit?

- If your guess is accurate and you hit a ship, the game will instantly notify you with a "Hit!" message
- The grid will update to show your successful hit, with the corresponding cell marked by an 'X' This mark indicates that a ship has been struck in that specific location
- The updated grid will appear, displaying the hit mark, allowing you to track your successful shots and adjust your strategy as needed

![Hit](/assets/images/hit.png)

### Game Progress After a Hit

- Following each hit, the game will proceed, giving you the opportunity to make your next guess
- The objective is to sink all 5 enemy ships before depleting your 15 available shots. Each successful hit brings you one step closer to victory
- If you manage to sink all the ships, the game will display a victory message congratulating you on your success in destroying all the enemy ships

### Game Over

The game ends when either all enemy ships have been sunk or you have exhausted all your available shots. Here’s what occurs in each scenario:

- Sinking All Ships:

    - If you manage to hit all 5 enemy ships before using up your 15 shots, the game will display a congratulatory message indicating that you have won. This means you’ve outsmarted the computer and successfully completed your mission

- Running Out of Shots:

    - If you exhaust all 12 shots without sinking all the enemy ships, the game will notify you with a "Game Over" message. This message will indicate that you’ve run out of shots and include a summary of your performance, detailing how many ships remain afloat
    - The game will then reveal to you where the remaining ships were

## Software Validation Testing

The code was tested using Code Institute's Python Linter for PEP8 compliance. Two errors' were identified:

- E501: Line too long — This issue arises when certain lines exceed the recommended length
- E302 expected 2 blank lines, found 1 — This issue I have researched and tried many ways to fix but have been unable to

I have checked the code to confirm that it operates correctly, even with these formatting exceptions.

![Code Institute Python Linter](/assets/images/ci_python_linter.png)

## Deployment

The project was deployed using GitHub pages. The steps to deploy using GitHub pages are:

1. Go to the repository on GitHub.com
2. Select 'Settings' near the top of the page.
3. Select 'Pages' from the menu bar on the left of the page.
4. Under 'Source' select the 'Branch' dropdown menu and select the main branch.
5. Once selected, click the 'Save'.
6. Deployment should be confirmed by a message on a green background saying "Your site is published at" followed by the web address.

The live link can be found here - [Battleship](https://battleships-vs-computer-d6d3e8954180.herokuapp.com/)

### Resources Used

- [W3Schools](https://www.w3schools.com/)
- [Stack Overflow](https://stackoverflow.com/)
- [Youtube](https://www.youtube.com/)
- [ChatGPT]

## Acknowledgments

The Code Institute slack community for their quick responses and very helpful feedback.
