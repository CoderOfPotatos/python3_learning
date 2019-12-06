import math
import random

operations = ["+","-","*","/"]

print("How many questions do you want to do?")
QNum = input()
print("You have chose",QNum,"questions!")
x = 1

while x  <= int(QNum):
    signN = random.randint(0,3)
    sign =  operations[signN]  
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    print("Question",x,"What is",num1, sign ,num2,"?")
    answer = input()
    if sign == "+":
        comAnswer = num1 + num2
    elif sign == "-":
        comAnswer = num1 - num2
    elif sign == "*":
        comAnswer = num1 * num2
    else :
        comAnswer = num1 / num2
    if int(answer) == int(comAnswer):
        print("Correct!")
    else :
        print("Incorrect")
    x = x+1







    

