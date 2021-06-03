
#Import the package random
import random

#Using function 
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    if answerNumber == 2:
        return 'It is decided'
    if answerNumber == 3:
        return 'Try Again'
    if answerNumber == 4:
        return 'Nope'
    if answerNumber == 5:
        return 'Who are you again'
    if answerNumber == 6:
        return 'Noooo!!!!!!!!!'
    if answerNumber == 7:
        return 'Im doubting for you'
    if answerNumber == 8:
        return 'You will have bad luck'
    if answerNumber == 9:
        return 'Yes it is'

print(getAnswer(random.randint(1,9)))