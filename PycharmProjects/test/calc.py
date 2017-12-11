
def add (x, y):

    "Add Function"
    return x + y

def substruct (x, y):
    "substruct Function"
    return x - y

def multiply (x, y):
    "multiply Function"
    return x*y

def divide (x, y):
    "divide Function"
    if y==0:
        raise ValueError('Can not divide by zero!')
    return x/y