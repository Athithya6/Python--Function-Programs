#program to take matrix input and print it
'''
R = int(input("Enter the number of rows:\n"))
C = int(input("Enter the number of columns:\n")) 
# Initialize matrix 
matrix = [] 
print("Enter the entries rowwise:\n") 
 # For user input 
for i in range(R):          # A for loop for row entries 
    a =[] 
    for j in range(C):      # A for loop for column entries 
        a.append(int(input())) 
    matrix.append(a) 
# For printing the matrix 
for i in range(R): 
    for j in range(C): 
        print(matrix[i][j], end = " ") 
    print() 
'''


'''
R=int(input("Enter the number of rows:\n"))
C=int(input("Enter the number of columns:\n"))
x=[]
y=[]

def mat_in(matrix):
    #Initialize matrix
    matrix=[]

    for i in range(R):     #Loop for row entries
        a=[]
        for j in range(C): #Loop for column entries
            a.append(int(input()))
        matrix.append(a)

    #Printing the matrix
    for i in range(R):
        for j in range(C):
            print(matrix[i][j],end=" ")
        print()

print("First matrix:\n")
mat_in(x)
print("Second matrix:\n")
mat_in(y)
'''

'''
a=[[91,67,32],
   [43,12,88],
   [54,7,26]]

b=[[29,10,57],
   [92,16,47],
   [30,65,89]]

s=[[0,0,0],
   [0,0,0],
   [0,0,0]]

for i in range(len(a)):
    for j in range(len(a[0])):
        s[i][j]=a[i][j]+b[i][j]

print("Resultant matrix:\n")
for y in s:
    print(y)
'''

#matrix addition
'''
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],end=" ")
        print()

R=int(input("Enter the number of rows:\n"))
C=int(input("Enter the number of columns:\n"))

matrix1=[[0 for j in range(0,C)] for i in range(0,R)]
matrix2=[[0 for j in range(0,C)] for i in range(0,R)]
sum_matrix=[[0 for j in range(0,C)] for i in range(0,R)]

def main():
    print("first matrix:\n")
    for i in range(0,R):
        for j in range(0,C):
            matrix1[i][j]=int(input("Enter an element:\n "))
    print("Matrix 1:\n")
    print_matrix(matrix1)

    print("second matrix:\n")
    for i in range(0,R):
        for j in range(0,C):
            matrix2[i][j]=int(input("Enter an element:\n "))
    print("Matrix 2:\n")
    print_matrix(matrix2)

    for i in range(0,R):
        for j in range(0,C):
            sum_matrix[i][j]=matrix1[i][j]+matrix2[i][j]
    print("Resultant matrix after addition:\n")
    print_matrix(sum_matrix)


main()
'''
