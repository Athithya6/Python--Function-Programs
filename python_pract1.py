'''
filename='Athithya1.txt'
with open(filename,'w') as f:
	f.write("Finally been assigned to a desk.\n I now have a proper system.")
with open(filename,'r') as f:
	lines=f.readlines()
for i in lines:
	print i
with open(filename,'a') as f:
	f.write("\n I think this just might be my masterpiece.\n You're gonna"
                " need a bigger boat.\n You're talkin to me?")

f=open("Athi.txt","r")
print f.readline()
f.close()


file=open('Athithya.txt','w')
with open('Athithya.txt','w') as f:
	f.write("L&T Technology Service")
with open('Athithya.txt','r') as f:
	lines=f.readlines()
for i in lines:
	print i



import os
#os.remove('Athithya.txt')
if os.path.exists('aparna.txt'):
	os.remove('aparna.txt')
else:
	print("This file does'nt exist")



n=int(input("Enter a limit:\n"))
sum=0
for i in range(n):
	sum=sum+i

print "The sum is:\n",sum



b=int(input("Enter the base value:\n"))

h=int(input("Enter the height value:\n"))
area=0.5*b*h
print "The area is : \n"
print area



a=int(input("Enter the first side:\n"))	
b=int(input("Enter the second side:\n"))	
c=int(input("Enter the third side:\n"))
s=0.5*(a+b+c)
area=s*(s-a)*(s-b)*(s-c)
print "Area is:\n",area



n=int(input("Enter any positive number:\n"))
p=n
sum=0
while p!=0:
	rem=p%10
	sum=sum+(rem*rem*rem)
	p=p/10
if sum==n:
	print "Armstrong Number"
else:
	print "Not an Armstrong number"



#fibonacci series
l=[]
num=int(input("Enter any number:\n"))
a=0
b=1
count=2
l.append(a)
l.append(b)
while count<num:
	c=a+b
	l.append(c)
	a=b
	b=c
	count=count+1
print(l)
'''

'''
#fibonacci series using recursion
l=[]
m=int(input("Enter a limit upto which you want to print fibonacci series:\n"))
if(m<0):
    print("Please enter positive integer only")
    exit()
def fibo(n):
    if(n<=1):
        return n
    else:
        return fibo(n-1)+fibo(n-2)

for i in range(m):
    l.append(fibo(i))

#fibo(m)
#print(l)


'''
l=[1,2,3,4,4,2,3,5,6,7,6,8,9,8,78,0,0,6,5,4]
k=set(l)
print k



a=set()
a={6,2,6,3,45,34,79,56,45,2,3,4,12,34,79}
print a

b=list(a)
print b


#to generate random numbers
import random
print random.randint(0,100)	
'''

'''
#find hcf

def hcf(a,b):
	for i in range(1,a+1):
		if a%i==0 and b%i==0:
			hcf=i
	print "The HCF of the given numbers is:\n",hcf		

r=int(input("Enter the first number:\n"))
s=int(input("Enter the second number:\n"))
hcf(r,s)				
'''
'''
#find lcm

def lcm(p,q):
	if p>q:
		larger=p
	else:
		larger=q
	while(True):
		if larger%p==0 and larger%q==0:
			lcm=larger
			break
	larger+=1
	print "The LCM of the given numbers is:\n",lcm

x=int(input("Enter the first number:\n"))
y=int(input("Enter the second number:\n"))
lcm(x,y)		
'''
