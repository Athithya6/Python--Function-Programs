'''
def prime(a):
	flag=0
	for i in range(2,a//2):
		if a%i==0:
			flag=1
	if flag==1:
		print "Not prime"
	else:
		print "Prime"				
prime(19)
prime(190)
'''	

'''
l=[]
def prime(a):

	flag=0
	for i in range(2,(a//2)+1):
		if a%i==0:
			flag=1
	if flag==0:
		l.append(a)
					




def primeseries(n):
	for j in range(2,n+1):
		prime(j)

x=int(input("Enter the number upto which you want to print:\n"))
primeseries(x)
print l
'''



'''
#biggest of 3 numbers#
a=int(input("Enter the value for a"))
b=int(input("Enter for b"))
c=int(input("Enter for c"))
if a>b:
	max1=a
else:
	max1=b
if c>max1:
	max1=c
	print c
else:
	print max1
'''

'''
#command line arguments
import os
import sys


a=sys.argv[1]
b=sys.argv[2]
c=sys.argv[3]
d=sys.argv[4]
e=sys.argv[5]
for i in range(1,len(sys.argv)):
	print sys.argv[i]
'''

'''
#factorial

num=int(input("Enter any positive integer:\n"))
f=1
for i in range(1,num+1):
	f=f*i
print "the factorial of num:\n", f
'''


#factorial using recursion
'''
def fact(n):
	if n==0 or n==1:
		return 1
	else:
		return(n * fact(n-1))

num=int(input("Enter any number"))
print fact (num)
'''

'''
s=raw_input("Enter any string:\n")
print s[0:]
print s[1:4]
print s[:-1]
print s[::-1]
print s[:3]
print s[:-3]
print s.split()
for i in s:
	print i
print s*10
'''

'''
l1=[1,2,34,56]
l2=["aparna",123,16]
l3=l1+l2
print l3
for i in l3:
	print i
l3[2:5]
l3[::-1]
'''

'''
t1=(1,2,3,4)
t2=(5,6,7,8)
t3=t1+t2
#print t3
#print t3*20
#t3[4]=67
print t3[5]
'''


#palindome

flag=0
palin2=" "
palin1=raw_input("Enter any string : \n")
l=len(palin1)

for  i in range(0,l):
	if palin1[i]!=palin1[l-i-1]:
		flag=1
if flag==1:
	print " it is not palindrome"
else:
	print "it is palindrome"
for j in palin1:
	palin2=j+palin2
print "reversed string is:\n",palin2		




