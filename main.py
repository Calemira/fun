import random
import math
number = random.randint(1,100)
print('square root of your number is', round(math.sqrt(number),3),'\n')
attempts = 0;
guess = int(input())
while True:
    if guess != number:
        print('you are not there yet! the number you are off when devided by 2 and cubed is equal to', round(pow((abs(guess-number))/2, 2), 2), '\n')
        attempts += 1
        scguess = int(input())
        if scguess != number:
            print('AHH too hard for you! not last tip: you are off now by', abs(scguess-number) , '\n')
            trdguess = int(input())
            if trdguess != number:
                print('Thats a bummer! You lost- the number was', number)
                break
            elif trdguess == number:
                print('finally! congrats')
                break
        elif scguess == number:
            print('not that bad :)')
            break
    elif guess == number:
        print('got it! you a pro')
        break
