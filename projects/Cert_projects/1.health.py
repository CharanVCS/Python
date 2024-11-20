import random
health =50
difficutly = 1

potion_health= int(random.randint(25,50)/difficutly)
health = health + potion_health
print(health)