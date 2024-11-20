import time, random
from string import punctuation

for i in range(10):
    print(random.choice(punctuation)*(i+1), end='\r')
    time.sleep(0.5)
