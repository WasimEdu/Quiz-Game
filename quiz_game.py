# created by: Wasim

print("Welcome to the Quiz Game!")

answer = input("Do you wanna play this Game (yes/no): ").lower()

score = 0

if answer != "yes":
    quit()

answer = input("What stand for RAM? ").lower()

if answer == "random access memory":
    score += 1
    print("Correct!")

else:
    print("Incorrect!")


answer = input("What stand for CPU? ").lower()

if answer == "central processing unit":
    score += 1
    print("Correct!")

else:
    print("Incorrect!")


answer = input("What stand for ROM? ").lower()

if answer == "read only memory":
    score += 1
    print("Correct!")

else:
    print("Incorrect!")


answer = input("What stand for GPU? ").lower()

if answer == "graphics processing unit":
    score += 1
    print("Correct!")

else:
    print("Incorrect")


print("You have given " + str(score) + " correct answer!")
print("Your got " + str( ((score/4) *100) ) + "%.")
