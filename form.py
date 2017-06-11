from Class1 import *
from form1 import *

Show_form()
while True:
      Reg=raw_input('Do you want register? (y/n): ')
      Reg=Reg.lower()
      if Reg!='y':
         print'Bye!'
         break
      elif Reg=='y':
          CheckItems()
          option=raw_input('Enter the option 1-4 :')  
          if option not in ['1', '2', '3', '4']:
             print'Wrong option {}'.format(option)
             continue
          print
          Hour=raw_input('How many hour(s)? :')
          hour=int(Hour)
          print
          CheckOption(option, hour)
          
       
