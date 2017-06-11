def Factorial(n):
    if n<0:
       print"Factorial is only defined for positive integers"
       return None
    elif  n==0:
       return 1
    else:
      return n*Factorial(n-1)

while True:
  try:
     print' '
     n=raw_input("Enter a number or blank to quit: ")
     if n=='':
       break
     n=int(n)
  except ValueError:
     print' '
     print"Hello! Factorial is only defined for integers!"
     print' '
  else:
     print' '
     print"The factorial of {} is {}".format(n,Factorial(n))
