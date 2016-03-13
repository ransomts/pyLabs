
'''
Detect a divide by zero error without checking if the denominator is zero
'''

def div_check(x, y):
    try:
        x / y
    except ZeroDivisionError:
        return True
    else:
        return False
