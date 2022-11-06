def Greeting(name):
    print(f'Hello {name}') if name else print(f'Hello Undefined')


name = input('Enter Your name: ')
Greeting(name)
