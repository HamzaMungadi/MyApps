import pprint
import birth
while True:
    print('Enter a name: (blank to quit)')
    name = raw_input()
    name=str(name)
    name=name.lower()
    if name == '':
        break

    elif name in birth.birthdays:
        print(birth.birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = raw_input()
        birth.birthdays[name] = bday
        pprint.pformat(birth.birthdays)
        birthfile=open('birth.py','w')
        birthfile.write('birthdays= '+pprint.pformat(birth.birthdays)+ '\n')
        birthfile.close()
        print('Birthday database updated.')
        continue
