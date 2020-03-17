'''
#finding area of circle
import math
r=float(input("Enter the radius of the circle"))
area=(math.pi*r*r)
print("area is : ",area)

#sum of squares of first n natural numbers
n=int(input("Enter the upper limit:\n"))
sum1=0
sum2=0
for i in range(1,n+1):
    sum1=sum1+i*i
    sum2=sum2+i*i*i

print("The required square sum is: ",sum1)
print("The required cube sum is: ",sum2)

#finding square root
import math
def sqr_root(num):
    i=0.000
    while(i*i<=num):
        i+=0.001
    i-=0.001
    return i

n=int(input("Enter any positive number:\n"))
print("The square root of the number is: ",round(sqr_root(n),2))

#finding compound interest
import math
p=int(input("Enter the principal:\n"))
r=float(input("Enter the rate of interest:\n"))
n=int(input("Enter the time period:\n"))
q=(1+(r/100))
a=p*((q)**n)
ci=a-p

print("The amount after ",n, " years is:\n",round(a,2))
print("The compound interest is:\n",round(ci,2))

#interchanging first and last elements of a list
a=[1,2,3,4,5,6,7,8,9]
p=a[0]
a[0]=a[-1]
a[-1]=p
print(a)

b=[1+2j,12-18j,-90j,-35,-336,-10,74j,667,-882+6j,1764,-43-56j]
b[0]=b[0]+b[-1]
b[-1]=b[0]-b[-1]
b[0]=b[0]-b[-1]
print(b)
'''





