#more python programs

#program to find e raised to various values
'''
import math
l1=[3,-3,9,-9]
l2=[]

for i in range(0,4):
	l2.append(math.exp(l1[i]))

print(l2)
'''

'''
import math
n=int(input("Enter no.of places to which you want to display e and pi:\n"))
res1=round(math.exp(1),n)
res2=round(math.pi,n)
print("Rounded value of e: ",res1)
print("Rounded value of pi: ",res2)
'''

'''
#Fibonacci series
n=int(input("Enter the no.of terms you want to print:\n"))
a=0
b=1
l=[]
l.append(a)
l.append(b)
for i in range(0,n):
	a,b=b,a+b
	l.append(b)
print("Fibonacci series:\n",l)
'''

'''
#Prime factors

def prime(n):
	count=0
	for i in range(1,n+1):
		if(n%i==0):
			count+=1
	
	if(count==2):
		return True
	else:
		return False

l=[]
m=int(input("Enter any positive number:\n"))
for i in range(1,m+1):
	if(m%i==0):
		l.append(i)

print("The prime factors of the given number are:\n")
print(list(filter(prime,l)))		
'''

'''
#cost of tiles to cover a floor
l=float(input("Enter the length of a tile(in metres):\n"))
b=float(input("Enter the breadth of a tile(in metres):\n")) 	
c=float(input("Enter the cost of one tile(in rupees):\n"))

t=l*b*c
print("Total cost of laying the floor: Rs.{}".format(round(t,2)))					
'''

'''
#Change return

c=float(input("Enter the total cost:\n"))
t=float(input("Enter the total amount given:\n"))
ch=t-c
print("Total change: ",ch)
ch1=int(ch/100)
ch2=int((ch-(ch1*100))/10)
ch3=round((ch-(ch1*100+ch2*10)))
print("No.of hundreds to be given: ",ch1)
print("No.of tens to be given: ",ch2)
print("NO.of one rupee coins to be given: ",ch3)
'''


