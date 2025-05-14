# Function==========================================================================

def add():

    x = 4
    y= 4
    result = (x+y)
    print(result)

add()

y = 'krishan'

def name(x):
    print('my Name is:', x)

name(y)



# Defining multiple function and callling in one function========================================


def add(x,y):
    print('add:', x+y)

def subtract(x,y):
    print('Subtract:', x-y)

def Multiply(x,y):
    print('Multpliction:', x*y)


num1 = 5
num2 = 7

def calculate():
    add(num1, num2)
    subtract(num1, num2)
    Multiply(num1, num2)

calculate()




    