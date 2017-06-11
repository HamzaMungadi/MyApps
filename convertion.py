def convert():
    while True:
       try:
           print"""
Enter 1 to convert from inches to cm
Enter 2 to convert from cm to m
Enter 0 to quit
"""
           respond=raw_input('>>>')
           respond=int(respond)
       except ValueError:
           print("{} isn't a number!".format(respond))
           break
       else:
           if respond== 1:
              try:
                 inches=raw_input("Provide the number of inches: ")
             
                 cm= float(inches)*2.54
                 massage="{} inches is {} centemeter".format(inches, cm)
                 inches=int(inches)
              except ValueError:
                  print("{} is not a number!".format(inches))
                  break
              else:
                  print massage
                  break
           elif respond==2:
                try:
		      cm=raw_input("Provide the number of cm: ")
		      m=100*cm
		      massage="{} centemeter is {} meter".format(cm, m)
                      cm=int(cm)
                except ValueError:
                     print("{} is not a number!".format(cm))
                     break
                else:
		      print massage
		      break
           elif respond==0:
              break
           else:
               print 'bye'
               break
        
convert() 
