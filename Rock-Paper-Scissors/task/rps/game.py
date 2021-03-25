import random


def save(name, score):
    ratings = open('rating.txt', "a", encoding='utf-8')
    ratings.write(name + " " + str(score) + "\n")
    ratings.close()
    return


def load(name):
    f = False
    lname = " "
    lscore = " "
    ratings = open('rating.txt', "r", encoding='utf-8')
    for line in ratings:
        lname, lscore = line.split(" ")
        if lname == name:
            f = True
            break
    ratings.close()
    if f:
        return int(lscore)
    else:
        return 0


# To create the file if it doesn't exist
ratings = open('rating.txt', "a", encoding='utf-8')
ratings.close()
#
name = input("Enter your name:")
print(f"Hello, {name}")
score = load(name)
correct = ["scissors", "paper", "rock", "!exit", "!rating"]
while True:
    choices = ["scissors", "paper", "rock"]
    ans = input()
    random.shuffle(choices)
    lose = None
    if ans not in correct:
        print("Invalid input")
    elif ans == "!exit":
        print("Bye!")
        break
    elif ans == "!rating":
        print(f"Your rating: {score}")
    elif ans == choices[0]:
        lose = -1
    elif ans == "scissors" and choices[0] == "rock":
        lose = 1
    elif ans == "paper" and choices[0] == "scissors":
        lose = 1
    elif ans == "rock" and choices[0] == "paper":
        lose = 1
    else:
        lose = 0
    if lose is not None:
        if lose == 1:
            print(f"Sorry, but the computer chose {choices[0]}")
        elif lose == 0:
            print(f"Well done. The computer chose {choices[0]} and failed")
            score += 100
        elif lose == -1:
            print(f"There is a draw ({choices[0]})")
            score += 50
        else:
            print("How?")
    save(name, score)
