from math import sqrt

print('Module `run_second` initialized')

def calc():
    a = int(input('Pick a number: '))
    b = int(input('Pick a second number: '))
    cal = pow(a, sqrt(pow(a, b)))
    print(cal)
    return cal
