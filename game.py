import word

class Game:

    # Local variables
    lives = 0

    # Construct the game
    def __init__(self, lives):
        # Initialize all variables
        self.lives = lives

    # Set the number of lives player has
    def set_lives(self):
        # Set the number of lives to seven
        self.lives = 7

# Create an instance of the 'Game' and 'Word' class
new_word = word.Word("", "")
hangman = Game(0)

# Function to display set the random word, display lives and blanks
def startGame():

   # Make both instances global
   global hangman, new_word

   # Call methods to setup the game
   hangman.set_lives()
   new_word.set_randomWord()
   new_word.set_blanks()

   # Print out the lives and blanks
   print("Lives: {}".format(hangman.lives))
   print(new_word.get_blanks)

# Call the method
startGame()

# Function to determine if user has won
def checkWin():

    # Local variables
    user_word = ""

    # Get the random word to be guessed
    word = new_word.get_randomWord

    # Get the blanks string and store in variable
    user_word = new_word.get_blanks

    # Remove all spaces from string
    user_word = user_word.replace(" ", "")

    # Return if both strings are equal
    return user_word == word


# Function to get user input
def get_userletter():

    # Local variables
    indexs = []

    # While lives is not equal to zero
    while hangman.lives != 0:
        # Ask user to input a letter
        user_letter = input("Please input a letter:\n")

        # Store the random word in variable
        word = new_word.get_randomWord

        # loop through word
        for i in range(0, len(word)):
            # Check if letter is equal to letter user inputed
            if word[i] == user_letter:
                # Store the index in array
                indexs.append(i)

        # Check if length of array is zero
        if len(indexs) == 0:
            # Decrease the number of lives by one
            hangman.lives -= 1
            # Recreate the indexs array
            indexs = []

            # Print out the lives and blanks to user
            print("Lives: {}".format(hangman.lives))
            print(new_word.get_blanks)
        else:
            # Call method within 'word' file to insert letter
            new_word.insert_letter(indexs, user_letter, hangman.lives)
            # Recreate the indexs array
            indexs = []

        # Call method to check if user has won
        if checkWin():
            print("You Win!")
            break

    # Check if lives are at zero
    if hangman.lives == 0:
        # Print to user they have lost
        print("You lose!")

# Call the method
get_userletter()

