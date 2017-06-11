from sys import argv
script, user_name=argv
prompt='>'

print"Hi %s am %s maigogo script"%(user_name, script)
print " "
print "%s I' d like ask you few questions" %(user_name)
print " "
print "how old are you %s" %(user_name)
age=raw_input(prompt)
print " "
print "Are you a student %s" %(user_name)
school=raw_input(prompt)
print"Do you like math"
math=raw_input(prompt)
print"Do you like programing"
programing=raw_input(prompt)
print"Do you like me"
likes=raw_input(prompt)
print "where do you live %s"% (user_name)
lives=raw_input(prompt)
print" Nice to meet you %s " %(user_name)
print" I ave recorded our chat with you %s"%(user_name)
print"enter yes to see and no to ignore"
print"""
congratulation! you're %s old, 
you said %s about schooling,
 you said %s about liking math, 
you said %s about like programing 
you said %s about liking me
and finaly you are living in %s
"""%(age, school, math, programing,likes, lives)
 
