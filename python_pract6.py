'''
a=[[1,2]]

b=[[0],
   [0]]

for i in range(len(a)):
    for j in range(len(a[0])):
        b[j][i]=a[i][j]

for l in b:
    print(l)

my_string=input("Enter any string:\n")
characters=my_string.split()
characters.sort()
for i in characters:
    print(i)

#fibonacci series and nth fibonacci number
l=[]
m=int(input("Enter the limit upto which you want to print the Fibonacci series:\n"))
def fibo(n):
    if(n<0):
        print("Invalid input")
    elif(n==0 or n==1):
        return n
    else:
        return fibo(n-1)+fibo(n-2)
   
for i in range(m):
    l.append(fibo(i))

print(l)
print("The required fibonacci number is: ",l[-1])



#program to find roots of quadratic equation
import math
import cmath
a,b,c=[int(x) for x in input("Enter the coefficients of the equation:\n").split()]
print("First coefficient is: ",a)
print("Second coefficient is: ",b)
print("Third coefficient is: ",c)
d=(b**2)-(4*a*c)
print("The discriminant is:\n",d)

if(d>0):
    print("Real and unequal roots")
    r1=(-b+math.sqrt(d))/(2*a)
    r2=(-b-math.sqrt(d))/(2*a)
    print("The roots are:\n",r1,r2)

elif(d==0):
    print("Real and equal roots")
    r=(-b/(2*a))
    print("The two roots are the same and are equal to:\n",r)

else:
    print("Imaginary roots")
    r1=(-b+cmath.sqrt(d))/(2*a)
    r2=(-b-cmath.sqrt(d))/(2*a)
    print("The roots are:\n",r1,r2)
    print("\n")

#finding vowels in a string
vowels="aAeEiIoOuU"
l1=[]
l2=[]
mystring=input("Enter any string:\n")
for letter in mystring:
    if letter in vowels:
        l1.append(letter)
    else:
        l2.append(letter)

print("The no.of vowels in the string are:\n",len(l1))
print("The vowels are:\n",l1)

print("The no.of consonants are:\n",len(l2))
print("The consonants are:\n",l2)
