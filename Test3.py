print('Guess a number')
i = 0
while (i < 9):
    i = i + 1
    n = int(input())
    if n > 21 :
        print('guess is wrong, enter a smaller no. \n''No of guess remains', 9 - i)
    elif n <21 :
        print('guess is wrong, enter a greater no. \n''No of guess remains', 9 - i)

    elif n == 21:

        print('congratulations \nyou won!️')
        break
else:
    print('Game is over\n you lose!!!')

