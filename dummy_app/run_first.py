from time import sleep

print('Module `run_first` initialized')

def say_hi():
    print('App started!')
    sleep(1)

def welcome():
    name = input('Please, enter your name: ')
    print('Computing..')
    sleep(2)
    print(f'Thanks for waiting, {name}')
    return name

