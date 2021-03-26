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
#
score = load(name)
#
choices = input().split(",")
if len(choices) == 1:
    choices = ["rock", "paper", "scissors"]
print("Okay, let's start")
#
compch = choices[:]
# to create a separate list
while True:
    #
    ans = input()
    #
    if ans == "!exit":
        print("Bye!")
        break
    #
    elif ans == "!rating":
        print(f"Your rating: {score}")
    #
    elif ans not in choices:
        print("Invalid input")
    #
    else:
        random.shuffle(compch)
        loc = choices.index(ans)
        winlist = choices[loc+1:]+choices[:loc]
        le = (len(winlist) / 2) - 1
        try:
            loc = winlist.index(compch[0])
            if loc > le:
                print(f"Well done. The computer chose {compch[0]} and failed")
                score += 100
            else:
                print(f"Sorry, but the computer chose {compch[0]}")
        except ValueError:
            print(f"There is a draw ({compch[0]})")
            score += 50
    #
    save(name, score)
