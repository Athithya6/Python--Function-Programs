"""
#printing all characters of a word
lst=[x for x in "Athithya"]
print(lst)

#printing squares of numbers between 1 and 100
sqr_lst=[x**2 for x in range(1,100)]
print(sqr_lst)

#printing multiples of 3
l=[x for x in range (1,100) if x%3==0]
print(l)


#converting inches to centimeters
l=[3,8.9,56.44,0.789,12.56]
c=[(print("The value in centimeters is:\n",(2.54*x)))for x in l]
c

#printing calendar
import calendar
y=int(input("Enter a year:\n"))
m=int(input("Enter a month:\n"))
print(calendar.month(y,m))

#converting miles to km
m=[45.67,88,93,12,24.3,33.8,56.21,64.9,78.23,4]
i=[(print("The value in km is:\n",0.62137*num)) for num in m]
i

#printing multiplication table
num=int(input("Which number's multiplication table do you want:\n"))
for i in range(1,21):
    print(num,'x',i,'=',num*i)

#convert a decimal number to octal,binary,hexadecimal
d=int(input("Enter a decimal number:\n"))

h=hex(d)
print("The equivalent hexadecimal number is:\n",h)

o=oct(d)
print("The equivalent octal number is:\n",o)

b=bin(d)
print("The equivalent binary number is:\n",b)

#printing ascii value of a character
c=input("enter any character")
print("the ASCII value of " + c +"  is   : ", ord(c))


#transpose of a matrix
R=int(input("Enter the number of rows:\n"))
C=int(input("Enter the number of columns:\n"))

matrix=[[int(input("Enter an element:\n")) for j in range(0,C)]for i in range(0,R)]
result=[[0 for j in range(0,C)]for i in range(0,R)]

for i in range(len(matrix)):
	for j in range(len(matrix[0])):
		result[i][j]=matrix[j][i]

for l in result:
	print(l)
"""
