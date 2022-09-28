print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")


if playing.lower() != "yes":
    quit()
print( "okay! Let's play :) ")
score = 0
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
answer = input(" What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("What is a stream? ")
if answer.lower() == "transmit or receive data over the internet as a steady, continuous flow":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("What is a class? ")
if answer.lower() == "a class is used to define the characteristics of an object ":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

print("You got  " + str(score) + " questions correct!")

