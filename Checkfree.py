import random

Num_digits = 3
Max_guesses = 10

def main():
    while True:
        secretNum = getSecretNum()
        print('I am thinking about a number')
        print('You have {} guesses to figure it out')
        numGuesses = 1
        while numGuesses <= Max_guesses:
            guess = ''
            while len(guess) != Num_digits or not guess.isdecimal():
                print('Guess #{}'.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > Max_guesses:
                print('Better luck next time')
                print('The answer was: {}'.format(secretNum))
        print('Do you wanna try again? (y)es or (n)o')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for the game')

def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretnum = ''
    for i in range(Num_digits):
        secretnum += str(numbers[i])
    return secretnum

def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it'
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__':
    main()