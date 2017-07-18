#from p1 import *
#from DinCalendar import *
#from DIN2017Calender import *
from programview import *

def show_months(programs):
    print'DIN PROGRAMS JULY-DECEMBER, 2017'
    print'-------------------------------'
    for i in range(len(programs)):
        month=programs[i]
        print str(i+1)+ '.  ' +month
    print
def show_programs(month):
    print'--------------------'
    print
    for prog in month:
       prog.display()
def main():
    print
    print'~~~~~~~~~~~~The DIN Viewer program~~~~~~~~~~~~~~'
    print
    print'Please enter the serial number of the month 1-6'
    print'to view all the programs in the month'
    print
    #a tuple of booker objects
    mp=['JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']
    show_months(mp)
    while True:
       try:
          try:
            number=int(raw_input('Enter a month serial number: '))
          except ValueError:
            print'Please enter a serial number of the month'
            print'Bye!'
            break
	  print
	  program=MONTHS[number-1]
	  show_programs(program)
       except IndexError:
           print'The number {} is out of range'.format(number)
       print
       choice=raw_input('View another month program(s)? (y/n): ')
       print
       if choice!='y':
          print'Bye!'
          break
main()
