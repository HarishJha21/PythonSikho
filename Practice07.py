import random

def guessGame(a, b, actual):
    guess=int(input(f"Guess a number between {a} and {b}\n"))
    nguess=1
    while guess!=actual:
        if guess<actual:
            guess=int(input(f"Enter a bigger number\n"))
            nguess+=1

        else:
            guess=int(input(f"Enter a smaller number\n"))
            nguess+=1

    print(f"You guessed the number in {nguess} guesses\n")
    return nguess


if __name__=="__main__":
    a=int(input("Enter the value of a\n"))
    b=int(input("Enter the value of b\n"))
    actual=random.randint(a, b)
    print("Player 1 Kheliye\n")
    g1=guessGame(a, b, actual)
    print("Player 2 Kheliye\n")
    g2=guessGame(a, b, actual)

    if g1<g2:
        print("Player 1 jeet chuke hai!\n")

    elif g1>g2:
        print("Player 2 jeet chuke hai!\n")

    else:
        print("Its a Tie!\n")


