from p1 import *
from DinCalendar import *
from DIN2017Calender import *

def show_programs(programs):
    print'2017 DIN/IET PROGRAMS'
    print'--------------------'
    for i in range(len(programs)):
        program=programs[i]
        print str(i+1)+ '.  ' +program.pName
    print
def show_program(program):
    print'PROGRAM IMFORMATION'
    print'--------------------'
    print
    program.Details()
def main():
    print'The DIN Viewer program'
    print
    #a tuple of booker objects
    programs=(prog1,prog2,prog3,prog4,prog5)
    show_programs(programs)
    while True:
       try:
          try:
            number=int(raw_input('Enter the program number: '))
          except ValueError:
            print'Please enter a number'
            print'Bye!'
            break
	  print
	  program=programs[number-1]
	  show_program(program)
       except IndexError:
           print'The number {} is out of range'.format(number)
       print
       choice=raw_input('View another program? (y/n): ')
       print
       if choice!='y':
          print'Bye!'
          break
main()
