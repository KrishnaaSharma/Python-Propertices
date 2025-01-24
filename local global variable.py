# local Variable

def var():
    local_var = 10
    print("local Variable:", local_var)
    
var()

# Global Variable

x =10

def var():
    print("global Variable:", x)

var()


var = 10

def my_function():
    print("Inside the function:", var)

my_function()

print("Outside the function:", var)