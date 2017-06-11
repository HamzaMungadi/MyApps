from p1 import *
from mytime import *
from tafsirhall import *
from TafsirHallRenting import *

def show_bookers(bookers):
    print'BOOKERS'
    for i in range(len(bookers)):
        booker=bookers[i]
        print str(i+1)+ '.  ' +booker.person
    print
def show_booker(booker):
    print'BOOKER DATA'
    booker.Display()
def main():
    print'The booking Viewer program'
    print
    #a tuple of booker objects
    bookers=(Booker1, Booker2,Booker3, Booker4, Booker5, Booker6, Booker7)
    show_bookers(bookers)
    while True:
           number=int(raw_input('Enter the Booker number: '))
	   print
	   booker=bookers[number-1]
	   show_booker(booker)
	   choice=raw_input('View another booker? (y/n): ')
	   print
	   if choice!='y':
	      print'Bye!'
	      break
main()
