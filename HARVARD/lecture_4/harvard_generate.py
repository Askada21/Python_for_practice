# Lecture 4: (Libraries)
# Random output
# import random
#from random import choice # Go to the random module and bring the choice function into my program. Import only the choice() function from the random module.
#coin = choice(["heads", "tails"])
#print(coin)

# Random Number
#import random
#number = random.randint(1, 10) # function will generate a random number between 1 and 10. 
#print(number)

# Random 3 choices
import random
cards = ["jack", "queen", "king"]
random.shuffle(cards) # shuffles a list into a random order. changes the order of the existing list.
for card in cards: # For each card inside cards, do something.
    print(card)