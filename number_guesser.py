# import the randorm module
import random

# this block of code checks if the top of range number is greater than zero and it is also a number
top_of_range = input("Enter a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range) # converting the string into a number

    if top_of_range <= 0:  # if the user entered a number less than zero (0)
        print("Please enter a number which is greater that 0 next time!")
        quit()
else:                      #if the user didn't enter a number
    print("Please type a number next time!")
    quit()

# The main program
random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_gueass = input("Make a gueass: ")   # prompt user to enter a number
    if user_gueass.isdigit():                  # check if entered number is a digit
        user_gueass = int(user_gueass)          # convert the entered number into a digit
    else:
        print("Please type a number next time!")
        continue

    if user_gueass == random_number:
        print("Correct! You guessed the correct number!")
        break

    elif user_gueass > random_number:
         print("Your guess is above the number! Try Again")
    else:
         print("Your guess is below the number! Try Again")

print(f"You got in {guesses} guesses!")