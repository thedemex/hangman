#import os
#os.system("pause") to stop the program (Windows only)

numWrong = 0 #number of wrong guesses so far
numTries = 6 #the total number of tries
ans = []     #the sentence solution
curAns = []  #the current solution, including the characters guessed by the player so far
gameOver = False

def change_curAns(char):
    for i in range(len(ans)):
        if(ans[i] == char):
            curAns[i] = char
        


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

def setup():
    show_hangman(numWrong)
    print('   ' + ' '.join(curAns) + '。')
    print('Please enter another character')

def main():
    global ans
    global numWrong

    #set correct answer
    print('Hello! Welcome to Hangman! Let\'s setup the game!')
    print('Type in the correct answer: ')
    ans = list(input())
    print('Let\'s begin!')

    #initial game setup
    for i in ans:
        curAns.append('_')
    show_hangman(numWrong)
    print('   ' + ' '.join(curAns) + '。')
    print('Please enter a character')
    
    #running game
    while (numWrong < numTries) and (curAns != ans):
        guess = input()
        if guess in ans:
            change_curAns(guess)
        else:
            numWrong += 1
            print('Sorry, that character is not in the answer.')
        setup()
    

    if(numWrong < numTries):
        print('Congratulations! You win!')
    else:
        print('\nSorry, you lose. The correct sentence was ' + ''.join(ans) + '。')

    
main()