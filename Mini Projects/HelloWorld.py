from string import digits, ascii_letters, punctuation
import random, time

word ='Hello, World!'
lts = digits + ascii_letters + punctuation + ' '
temp=''
i = 0

while True:
    j = random.choice(lts)
    print(temp+j)
    if j is word[i]:
        temp+=j
        i+=1
      
    if temp == word:
        break
    time.sleep(0.005)
end = input ('press enter key to exit')