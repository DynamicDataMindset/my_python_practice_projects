print("THIS IS A PROGRAM WHICH ASKS FOR A USER TO ANTER ANY NUMBER AND TELLS THE USER IF ITS ODD OR EVEN NUMBER!")

num = int(input("Please enter any number from 1 to infinity: "))

if num % 2 == 0:
    print(f"Your number is: {num} and it is an even number.")
else: 
    print(f"Your number is: {num} and it is an odd number.")

