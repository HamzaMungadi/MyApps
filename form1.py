from Class1 import *
#from form import *
def Show_form():
    print
    print'Items for renting tafsir Hall'
    print
    print 'S/N   Facility                 Rate             Comment'
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print '1.    Tafsir Hall         -->  N{} per hour   Non-Refundable'.format(Re.TafsirHall)
    print '2.    Generator           -->  N{} per hour   Refundable'.format(Re.Generator)
    print '3.    Class Room          -->  N{} per hour   Non-Refundable'.format(Re.ClassRoom)
    print '4.    General Cleaning    -->  N{} per hour   Non-Refundable'.format(Re.Gcleaning)
    print '5.    Deposite for Dimage -->  N{} per hour   Refundable'.format(Re.DepositeForDamage)
    print '6.    P.A.S               -->  N{} per hour   Non-Refundable'.format(Re.PAS)
    print 
def CheckOption(option,hour):
    Hall=Re.TafsirHall*hour
    Gen=Re.Generator*hour
    P=Re.PAS*hour
    Total=Hall+Gen+P+Re.ClassRoom+Re.DepositeForDamage+Re.Gcleaning
    Total2=Total-P
    Total3=Total-Re.ClassRoom
    Total4=Total-(Re.ClassRoom+P)
    if option=='1':
       print
       print'Thank you for register'
       print'The total money to be paid is N{} for {} hour(s)'.format(Total, hour)
       print 
       print'Here is the detail payment'
       print
       print '1. Tafsir Hall         --> {} '.format(Hall)
       print '2. Generator           --> {} '.format(Gen)
       print '3. Class Room          --> {} '.format(Re.ClassRoom)
       print '4. General Cleaning    --> {} '.format(Re.Gcleaning)
       print '5. Deposite for Dimage --> {} '.format(Re.DepositeForDamage)
       print '6. P.A.S               --> {}  '.format(P)
       print
       print '~~Total Amount~~       --> {}   '.format(Total)
       print
    elif option=='2':
       print
       print'Thank you for register'
       print'The total money to be paid is N{} for {} hour(s)'.format(Total2, hour)
       print 
       print'Here is the detail payment'
       print
       print '1. Tafsir Hall         --> {} '.format(Hall)
       print '2. Generator           --> {} '.format(Gen)
       print '3. Class Room          --> {} '.format(Re.ClassRoom)
       print '4. General Cleaning    --> {} '.format(Re.Gcleaning)
       print '5. Deposite for Dimage --> {} '.format(Re.DepositeForDamage)
       print '6. P.A.S               --> NO  '
       print
       print '~~Total Amount~~       --> {}   '.format(Total2)
       print
    elif option=='3':
       print
       print'Thank you for register'
       print'The total money to be paid is N{} for {} hour(s)'.format(Total3, hour)
       print 
       print'Here is the detail payment'
       print
       print '1. Tafsir Hall         --> {} '.format(Hall)
       print '2. Generator           --> {} '.format(Gen)
       print '3. Class Room          --> NO '
       print '4. General Cleaning    --> {} '.format(Re.Gcleaning)
       print '5. Deposite for Dimage --> {} '.format(Re.DepositeForDamage)
       print '6. P.A.S               --> {}  '.format(P)
       print
       print '~~Total Amount~~       --> {}   '.format(Total3)
       print
    elif option=='4':
       print
       print'Thank you for register'
       print'The total money to be paid is N{} for {} hour(s)'.format(Total4, hour)
       print 
       print'Here is the detail payment'
       print
       print '1. Tafsir Hall         --> {} '.format(Hall)
       print '2. Generator           --> {} '.format(Gen)
       print '3. Class Room          --> NO '
       print '4. General Cleaning    --> {} '.format(Re.Gcleaning)
       print '5. Deposite for Dimage --> {} '.format(Re.DepositeForDamage)
       print '6. P.A.S               --> NO  '
       print
       print '~~Total Amount~~       --> {}   '.format(Total4)
       print
def CheckItems():
    print 
    print'Please select the option below'
    print
    print'Enter 1 for use of all the items'
    print'Enter 2 to exclude a P.A.S'
    print'Enter 3 to exclude a class room'
    print'Enter 4 to exclude the class room and P.A.S'
    print 


