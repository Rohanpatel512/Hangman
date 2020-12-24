import random

class Word:

    # Local variables
    random_word = ""
    blanks = ""

    # Construct the word
    def __init__(self, random_word, blanks):
        # Initialize the random word
        self.random_word = random_word
        self.blanks = blanks

    # Sets the random word
    def set_randomWord(self):
        # Create an array of words to choose from
        words = ["laptop", "computer", "keyboard", "camera", "tablet"]

        # Get index of random word and store in variable
        index = random.randint(0, 4)

        # Get the random word and store in variable
        self.__random_word = words[index]


    # Sets the number of blanks to be displayed
    def set_blanks(self):

        # Make the global variable 'blanks' global
        global blanks

        # Recreate the name variable
        word = self.__random_word

        # Loop through the word
        for letters in word:
            # Replace each letter with a blank
            word = word.replace(letters, " ̶")

        # Store the blanks in variable
        self.__blanks = word

    # Inserts letter inside the blanks
    def insert_letter(self, indexs, letter, lives):
        # Split the blanks string into array
        self.__blanks = self.__blanks.split(" ")

        # Check if there is a blank space in array
        if ' ' in self.__blanks:
            # Remove a blank spot from the array
            self.__blanks.remove(' ')

        # Loop through the blanks array
        for i in range(0, len(self.__blanks)):
            # Check if value of i is in indexs array
            if i in indexs:
                self.__blanks[i + 1] = ""
                self.__blanks[i + 1] = letter

        # Turn array back into string and store in variable
        self.__blanks = " ".join(self.__blanks)

        # Print out the lives and blanks to user
        print("Lives: {}".format(lives))
        print(self.__blanks)


    @property
    def get_randomWord(self):
        # Return the random word
        return self.__random_word

    @property
    def get_blanks(self):
        # Return the blanks
        return self.__blanks