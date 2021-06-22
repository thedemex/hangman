#import os
#os.system("pause") to stop the program (Windows only)

numWrong = 0 #number of wrong guesses so far
numTries = 6 #the total number of tries
ans = []     #the sentence solution
curAns = []  #the current solution, including the characters guessed by the player so far

def show_sentence():

def show_hangman(state):
    states = ["""
        --------
        |     |
        |
        |
        |
        |
        |_________
            """, 
            """
        --------
        |     |
        |     O
        |
        |
        |
        |_________
            """,
             """
        --------
        |     |
        |     O
        |     |
        |     |
        |
        |_________
            """,
             """
        --------
        |     |
        |     O
        |   \\ |
        |     |
        |
        |_________
            """,
              """
        --------
        |     |
        |     O
        |   \\ | /
        |     |
        |
        |_________
            """,
              """
        --------
        |     |
        |     O
        |   \\ | /
        |     |
        |    /
        |_________
            """,
              """
        --------
        |     |
        |     O
        |   \\ | /
        |     |
        |    / \\
        |_________
            """]
    print(states[state])

#show_hangman(6)