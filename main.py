print("Welcome to Taylor Swift Quiz ")
playing = input("This game is for Taylor's Fan! Wanna play? ")

if playing.lower() != "yes" :
    quit()

print("Okay! Let the game Begin!! ")
score = 0
count = 0

answer = input("What is Taylor Swift Favourite number? ")
if answer == "13" :
    print("Correct!")
    score += 13
    count += 1
else:
    print("Incorrect!")

answer = input("What is Taylor Swift middle name? ")
if answer.lower() == "alison" :
    print("Correct!")
    score += 13
    count += 1
else:
    print("Incorrect!")

answer = input("In which month Taylor Swift born? ")
if answer.lower() == "december" :
    print("Correct!")
    score += 13
    count += 1
else:
    print("Incorrect!")

answer = input("How many Sibling does Taylor have? ")
if answer.lower() == "1" :
    print("Correct!")
    score += 13
    count += 1
else:
    print("Incorrect!")

answer = input("How many grammys has she won? ")
if answer == "10" :
    print("Correct!")
    score += 13
    count += 1
else:
    print("Incorrect!")

answer = input("what year was Taylor born? ")
if answer == "1989" :
    print("Correct!")
    score += 13
    count += 1
else:
    print("Incorrect!")

answer = input("How many Albums has Taylor released? ")
if answer == "9" :
    print("Correct!")
    score += 13
    count += 1
else:
    print("Incorrect!")

answer = input("What was Taylor's first album? ")
if answer.lower() == "taylor swift" :
    print("Correct!")
    score += 13
    count += 1
else:
    print("Incorrect!")

answer = input("First pop album of Taylor Swift? ")
if answer == "1989" :
    print("Correct!")
    score += 13
    count += 1
else:
    print("Incorrect!")

print("you got " + str(score/13)+ " questions Correct.")
print("you got " + str((count / 9) * 100) + "%.")
