#import os
#os.system("pause") to stop the program (Windows only)

numWrong = 0 #number of wrong guesses so far
numTries = 6 #the total number of tries
ans = []     #the sentence solution
curAns = []  #the current solution, including the characters guessed by the player so far
gameOver = False

def change_curAns(tries):
    print(ans[tries])

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

def main():
    global ans

    #set correct answer
    print('Hello! Welcome to Hangman! Let\'s setup the game!')
    print('Type in the correct answer: ')
    ans = input()
    print('Let\'s begin!')

    #game setup
    for i in range(len(ans)):
        curAns.append('_')
    
    show_hangman(numWrong)
    print('   ' + ' '.join(curAns))
    print('Please enter a character')


main()