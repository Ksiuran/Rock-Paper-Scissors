# Stage 1, used to break the ice and have somewhere to start
import random

choices = ["scissors", "paper", "rock"]
ans = input()
random.shuffle(choices)
lose = None
if ans == choices[0]:
    lose = -1
elif ans == "scissors" and choices[0] == "rock":
    lose = 1
elif ans == "paper" and choices[0] == "scissors":
    lose = 1
elif ans == "rock" and choices[0] == "paper":
    lose = 1
else:
    lose = 0
if lose == 1:
    print(f"Sorry, but the computer chose {choices[0]}")
elif lose == 0:
    print(f"Well done. The computer chose {choices[0]} and failed")
elif lose == -1:
    print(f"There is a draw ({choices[0]})")
else:
    print("How?")
