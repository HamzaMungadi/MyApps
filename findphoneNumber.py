import re

phoneNumber=re.compile(r'(\+234)[7-9][0-1]\d{8}|0[7-9][0-1]\d{8}')

while True:
     print"Enter a text to search a phone no or blank to quit"
     respond=raw_input(">>>")
     if respond=='':
        break
     else:
        if respond!='':
           search=phoneNumber.search(respond)
           if search==None:
              print"Phone number not found in your taxt."
           else:
              print"Phone number found: "+search.group()
        
