import random, sys

Heart = chr(9829)
Diamonds = chr(9830)
Spades = chr(9824)
Clubs = chr(9827)

def main():
    print("What's your budget?")
    money = input()
    print("Your money is, ",money)

    while True:
        if money<0:
            print("Go home, get some more, 'cause you are poor")
            print("Better luck next time, I'm kidding it won't help on you! ")
            sys.exit()
        print("Your bet is: ",money)
        bet = getBet(money)