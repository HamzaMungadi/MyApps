Dicitems={}

def show_help():
    print"This is a sample program to make a table with 2 colom"
    print"""
Enter 'DONE' to stop adding items and value in the table.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current table.
"""

def show_table():
    print"Here is your table."
    table(Dicitems)

def Add_item_value(item, value):
    Dicitems.setdefault(item, value)
    print"Added {} in the table with value {}".format(item, value)

def table(Dicitem):
    print 'items of your table'.center(30,'-')
    for k,v in Dicitems.items():
        print(k.ljust(20,'.') +str(v).rjust(6))

show_help()
while True:
   item=raw_input('>>>') 
   #be able to control the app
   if item=='DONE':
      break
   elif item=='SHOW':
      show_table()
      continue
   elif item=='HELP':
      show_help()
      continue
   else:
       if item!='DONE':
          value=raw_input('Enter the value of '+item+' :')
          Add_item_value(item, value)
show_table()


