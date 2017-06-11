from sys import argv
import time
script, filename=argv

text=open(filename)
print"Here is the content of your file %r" %filename
print text.read()
print"Enter a filename again"
file_again=raw_input(">>>")
text1=open(file_again)
print"Here is what you have in %r" %file_again
print text1.read()
