print('-------- Positional Argument ------------')

def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet("Roger", 30)  

print()# Hello, Roger! You are 30 years old.

#================================================================================================

def show(name, age):
    print(name,age)

show("roger",30)

print() # roger 30

# 2.keybord Agrument================================================================

def show(name, age):
    print(age, name)

show("Steve", 20) # 20 Steve

# 3.Default Agrument================================================================================

def show(x, y=400, z=100):
    print(x,y,z)

show(100,200,300)

print()# 100 200 300



def show(x, y=400, z=100):
    print(x,y,z)

show(100,200)

print()# 100 200 100

# 4.Variable length argument=============================================================================

def show(*ages):
    print(ages[0],ages[1])

show(100,200)
print() # 100, 200


def show(*ages):
    print(ages[1],ages[0])

show(100,200)
print() # 200, 100


def show(*ages):
    print(ages[0],ages[1])

show(100,200,300,400)

print()# 100, 200


#5.Keyword Variable length argument:==============================================================

def show(**ages):
    print(ages['a'],ages['c'])

show(a=100,b=200,c=300)

print() # 100 300

# Global Function=============================================================================

x =300

def show():
    x= 200
    z=globals()['x']
    print("inside function ",x)
    print("inside function ",z)

show()
print("outside function",x)

print()

#inside function  200
#inside function  300
#outside function 300


# Global Keyboard====================================================================================

x =100  

def show():
    global x
    x= 200
    print("inside function ",x)
    print("inside function ",x)

show()

print("outside function",x)

print()

#inside function  200
#inside function  200
#outside function 200




