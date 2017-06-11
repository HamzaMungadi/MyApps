while True:
    print('Who are you?')
    name = raw_input()
    if name != 'Hamza':
        continue
    print('Hello, Hamza. What is the password? (It is a Town.)')
    password = raw_input()
    if password == 'Mungadi':
        break
print('Access granted.')
