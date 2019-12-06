import math
import random
name = input("What's your name? --> ")
print("\r")
print("Hello,",name, ", This will be a Math Test that will test your math skill")
print("\r")
print("The first section will be mutilplication")
print("\r")
score = 0

firstN = random.randint(1, 5)
secondN = random.randint(1, 5)
answer = firstN * secondN


print("First Question : What is %d multiply %d? --> "%(firstN, secondN ))
firstQ = input()
if firstQ == str(answer):
    print("Correct!")
    score = score + 1
else: print("Sorry, Incorrect")

firstN2 = random.randint(1, 5)
secondN2 = random.randint(1, 5)
answer2 = firstN2 * secondN2


print("Second Question : What is %d multiply %d? --> "%(firstN2, secondN2 ))
secondQ = input()
if secondQ == str(answer2):
    print("Correct!")
    score = score + 1
else: print("Sorry, Incorrect")


firstN3 = random.randint(3, 10)
secondN3 = random.randint(3, 10)
answer3 = firstN3 * secondN3


print("Third Question : What is %d multiply %d? --> "%(firstN3, secondN3 ))
thirdQ = input()
if thirdQ == str(answer3):
    print("Correct!")
    score = score + 1
else: print("Sorry, Incorrect")

firstN4 = random.randint(3, 10)
secondN4 = random.randint(3, 10)
answer4 = firstN4 * secondN4


print("Fourth Question : What is %d multiply %d? --> "%(firstN4, secondN4 ))
fourthQ = input()
if fourthQ == str(answer4):
    print("Correct!")
    score = score + 1
else: print("Sorry, Incorrect")

firstN5 = random.randint(3, 10)
secondN5 = random.randint(3, 10)
answer5 = firstN5 * secondN5


print("Fifth Question : What is %d multiply %d? --> "%(firstN5, secondN5 ))
fifthQ = input()
if fifthQ == str(answer5):
    print("Correct!")
    score = score + 1
else: print("Sorry, Incorrect")

print("Your score was", score / 5 *100 ,"percent")



    

