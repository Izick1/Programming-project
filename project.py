import random

secret_number = random.randrange(1,10)
guess_count= 0
guess_limit = 6
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count +=1
    if(guess > secret_number):
        print("Your Guess is higher than the secret number")   
    elif (guess < secret_number):
        print("Your Guess is lower than the secret number") 
    elif guess == secret_number:
        print('You won')
        break
else:
    print('sorry you failed, the secret number is: ', secret_number)