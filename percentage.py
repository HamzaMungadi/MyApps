def show_help(name):
    print("Hi "+name + " welcome to percentage Apps")

def To_amount(n, A):

     return (n/100)* A

def To_percent(TA, A):

     return (A*100)/TA

user=raw_input('What is your name? :')
show_help(user)

while True:
      print"""
Enter "P" to convert an amount to percentage
Enter "A" to convert a percentage to amount
Enter "C" to quit the Apps
"""
      ans=raw_input(">>>")
      ans=ans.upper()
      if ans=='C':
        break
      elif ans=='P':
         try:
            TA=raw_input("Enter total amout: ")
            TA=float(TA)
         except ValueError:
            print"Please provide a number"
         else:
           try:
              A=raw_input("Enter the amount you want to convert in percentage: ")
              A=float(A)
           except ValueError:
              print"Please provide a number"
           else:
              print To_percent(TA,A)
       
      elif ans=='A':
         try:
            A=raw_input("Enter total amout: ")
            A=float(A)
         except ValueError:
            print"Please provide a number"
         else:
           try:
              n=raw_input("Enter the number of percentage: ")
              n=float(n)
              if n>100:
                 print"Number of percentage can not exceed 100"
                 break
              elif n<0:
                 print"Number must be nonnegative"
                 break
              print To_amount(n, A)
           except ValueError:
              print"Please provide a number"
              
      
      else:
          print"Oops! the {} option you enter is not available".format(ans)    
