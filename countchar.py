import pprint 

count={}
while True:
     print"Enter your massage or blank to quit"
     massage=raw_input(">>>")
     if massage=='':
        break
     else:
        for char in massage:
            count.setdefault(char, 0)
            count[char]=count[char]+1
     pprint.pprint(count)
     
