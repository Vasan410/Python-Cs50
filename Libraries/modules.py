# random (random.choice())

'''import random
coin = random.choice(["heads", "tails"])
print(coin)'''

# Using from keyword

'''from random import choice
coin = choice(["heads", "tails"])
print(coin)
'''
# generating random numbers (random.randint()) 

'''import random
number = random.randint(1,20)
print(number)'''

# shuffling cards (random.shuffle())

import random
cards = ["king", "queen", "jack"]
random.shuffle(cards)
for card in cards:
    print(card)

