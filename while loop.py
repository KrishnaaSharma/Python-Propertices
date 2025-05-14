# create table============================================================================

n = int(input("Enter you number:"))
num = 5
i = 1

while i <= 10:
    print(n,'*',i, '=',n*1)
    i += 1

# hellp print===================================================================

i = 1
while i<100:
    print("hello",i)
    i +=1


# Rverse Values Print==================================================================

i = 100
while i>1 :
    print("Rverse Values",i)
    i-=1

n = int(input("Enter Your Number:"))

i = 1
while i<=10:
    print(n,'*',i, '=', n*i)
    i +=1

#Q. Print the element of the following list using a loop:======================================

[1,4,9,16,25,36,64,81,100]

nums = [1,4,9,16,25,36,64,49,81,100]

i =0
while i< len(nums):
    print(nums[i])
    i += 1



# Q. Armstrong===========================================================================

num = int (input("Enter your Armstrong Number:"))

sum =0
tep =num
while tep>sum :
    digit = tep %10
    cube = digit **3
    sum = sum + cube
    tep//10

if sum == sum:
    print("Armstrong is a number")
else :
    print("Armstrong is not number")

#Q. Sum Of digit=============================================================

i= int (input("Enter your Number:"))

sum =0
while i>0:
    sum = sum +i%10
    i=i//10
    print("sum of digit",sum)


#Q. Factorial Number=======================================================================

n = int(input("enter your number:"))

fact =1 
i=1

while(i<=n):
    fact = fact*i
    i +=1
    print('factorial is', fact)



