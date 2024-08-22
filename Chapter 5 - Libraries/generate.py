# Random Module
import random
# from random import choice

# Generate a random choice between "heads" and "tails" using the random.choice() function from the random module.

# coin = random.choice(["heads", "tails"])
# print(coin)


# Generate a random integer between 1 and 10 using the random.randint() function from the random module.

# random_number = random.randint(1, 10)
# print(random_number)

# Generate a random shuffle string using the random.shuffle() function from the random module.

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)


