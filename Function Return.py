
# def display():
#     return "Hello Word"
# print(display())

# display()

#---------------------------------------
def add_number(x, y):
    result = x+y
    return result

print(add_number(4, 5)) # 9

print()
#----------------------------------------
def number(x, y):
     result = x -y
     return result

sub = number(9, 9)

print(sub) # 0

print()

#--------------------------------


def show(x, y):
     add = x + y
     sub = x- y
     return add, sub


x,y = show(29, 93)

print(x, y) # 122, -64





print('------Nested Function------')
def outer_function():
    def inner_function():
        print('Innner Function')
    print('Outer Function')
    inner_function()
# Call the outer function
outer_function()

print()