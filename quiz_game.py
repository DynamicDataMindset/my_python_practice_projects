# Welcome statement
print("Welcome to my computer Quiz!")

playing = input("Do you want to play? ")

#if answer is not yes, the program stops or ends
if playing.lower() != "yes":
    quit()

print("Okay! Lets play")

# The main program
score = 0

answer = input("What does a CPU stand for? ").lower()
if answer == "central processing unit":
    print("CORRECT!!")
    score += 1
else:
    print("INCORRECT!!")

answer = input("What does a GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("CORRECT!!")
    score += 1
else:
    print("INCORRECT!!")

answer = input("What does a RAM stand for? ").lower()
if answer == "random access memory":
    print("CORRECT!!")
    score += 1
else:
    print("INCORRECT!!")

answer = input("What does a ROM stand for? ").lower()
if answer == "read only memory":
    print("CORRECT!!")
    score += 1
else:
    print("INCORRECT!!")

print(f"You got {score} questions correct!!") # Prints out the score
print(f"That is {score / 4 * 100}%") # Calculates the percantage