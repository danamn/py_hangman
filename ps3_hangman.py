# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "D:\DanaHTML\EdX CS Python\Week3ProblemSet\words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    result = list(secretWord)
    for letter in lettersGuessed:
        if letter in result:
            result = [x for x in result if x!= letter]
    return result == []





def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    result = secretWord
    notGuessedLetters = notGuessed(secretWord, lettersGuessed)   
    for letter in secretWord:
        if letter in notGuessedLetters:
            result = result.replace(letter, "_ ")
    return result



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    
    alphabet = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        if letter in alphabet:
            alphabet.remove(letter)
    return ''.join(alphabet)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    def notGuessed(secretWord, lettersGuessed):
        notGuessedLetters = list(secretWord)
        for letter in lettersGuessed:
            if letter in notGuessedLetters:
                notGuessedLetters = [x for x in notGuessedLetters if x!= letter]
        return notGuessedLetters   
    
    print("Welcome to the game, Hangman!"  + '\n' \
    + "I am thinking of a word that is " +str(len(secretWord))+" letters long. \n-------------")
    
    leftGuesses = 8
    lettersGuessed = []
    endGame = isWordGuessed(secretWord, lettersGuessed)    
  
        
    while leftGuesses > 0 and not endGame:
        availableLetters = getAvailableLetters(lettersGuessed)
        print('You have '+str(leftGuesses)+' guesses left.\nAvailable letters: '+availableLetters)
        letter = input('Please guess a letter: ').lower()
        guessedWord = getGuessedWord(secretWord, lettersGuessed)
        
        if letter in lettersGuessed:
           print("Oops! You've already guessed that letter: "+guessedWord+"\n------------\n")
        else:
            lettersGuessed.append(letter)
            guessedWord = getGuessedWord(secretWord, lettersGuessed)
            if letter in secretWord:       
                print("Good guess: " + guessedWord +"\n------------\n")
                endGame = isWordGuessed(secretWord, lettersGuessed)
            else:
                print('Oops! That letter is not in my word: '+ guessedWord+"\n------------\n")
                leftGuesses -=1
    else:
        if endGame:
            print("Congratulations, you won!")         
        elif leftGuesses<=0:
            print("Sorry, you ran out of guesses. The word was "+secretWord+".")

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
