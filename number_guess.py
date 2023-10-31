import random

def guess_number():
    secretNumber = random.randint(1,100)
    attempt = 0

    print("I have a number in mind. This number is between 1 and 100.")

    while True:
        try:
              #ask user for their guess.
            guess = int(input("Guess the number: "))
            attempt += 1

            #make the comparison
            if guess < secretNumber:
                print("Try a bigger number")
            elif guess > secretNumber:
                print("Try a smaller number")
            else:
                print(f"You have guessed the right number. You got it right on your {attempt} guess.")
                break

        except ValueError:
            print("Invalid input. Enter an integer")     

      

guess_number()