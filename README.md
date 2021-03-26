# Rock-Paper-Scissors
Project complete, Has score/rating saving, enter your name at start, next input is what you want to play with, leave it empty to go with the default rock paper scissors, else input the elements you would like to play with like so "rock,paper,scissors" or "rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,snake,scissors,fire", the number of elements you play with should be odd. "!exit" and "!rating" are extra commands, exit quits the game, rating outputs your current rating, you gain 50 for ties, 100 for wins.

What wins against what is determined by it's place in the list, using [rock, paper, scissors] as an example, say you chose rock, it creates a new list, [paper, scissors], everything with an index over the 1/2 mark loses to you, whereas everything below wins against you, another example would be you picking paper, the list it would create then would be [scissors, rock], the 1/2 rule holds true here, too. this reordering is achieved by taking everything after the one you chose and moving it to the front of the list. another example that better illustrates this would be using the 15 option game above, say you chose air, it would create a list like this [paper, sponge, wolf, tree, human, snake, scissors, fire, rock, gun, lightning, devil, dragon, water], everything over the 7th choice, scissors, loses to air, while everything including the 7th and below beats you.

An example output from running the game, > indicates uer input:
Enter your name: >Wilson
Hello, Wilson
>
Okay, let's start
>rock
Sorry, but the computer chose paper
>!exit
Bye!
