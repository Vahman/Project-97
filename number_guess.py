import random
answer=random.randint(1,9)
guess=int(input("Guess a number from 1-9: "))
is_guess_correct=False
if guess==answer:
    print("You guessed the number!")
    is_guess_correct=True
else:
    while not is_guess_correct:
        
        if guess==answer:
            print("You guessed the number!")
            is_guess_correct=True
            break
        else:
            if guess>answer:
                
                guess=int(input("Your guess is too large: "))

            else:
                guess=int(input("Your guess is too small: "))


