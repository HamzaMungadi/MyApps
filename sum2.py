import random
from sys import argv

script, user_name=argv

def displayIntro():
    print'Wellcome to mathe quiz play %s!' %user_name
    print' '
def AddPlay():
    number1=random.randint(1,10)
    number2=random.randint(1,10)
    print'What is ' + str(number1)+'+'+ str(number2)+'?'
    answer=raw_input()
    answer=int(answer)
    if answer==number1+number2:
        print'Correct!'
        print' '
    else:
        print'Nope! The answer is ' + str(number1+number2)
        print' '
def timesPlay():
    number1=random.randint(1,10)
    number2=random.randint(1,10)
    print'What is ' + str(number1)+'*'+ str(number2)+'?'
    answer=raw_input()
    answer=int(answer)
    if answer==number1*number2:
        print'Correct!'
        print' '
    else:
        print'Nope! The answer is ' + str(number1*number2)

playAgain='yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    AddPlay()
    AddPlay()
    timesPlay()
    timesPlay()
    print' '
    print('%s do you want to play mathe quiz again?  (yes or no)') %user_name
    playAgain = raw_input()
