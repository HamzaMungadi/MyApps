from sys import argv
import os
script, username=argv
while True:
    filename=raw_input("Enter a file name pls: ")
    check_exist=os.path.exists(filename)
    if check_exist:
        print"file exists"
        filename=open(filename, 'r+')
        print"Do you want read or write to file"
        answer=raw_input(">>>")
        if answer=='read':
           print "Here is the content of your file %r" %filename
           print filename.read()
        elif answer=='write':
           txt=raw_input("Enter the text to write:")
           filename.write(txt)
           filename.close()
        break
    else:
        print"file dosn't exist"
        break

