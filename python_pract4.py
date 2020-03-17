#matrix multiplication
#taking input for number of rows and columns
R1=int(input("Enter the number of rows for first matrix:\n"))
C1=int(input("Enter the number of columns for first matrix:\n"))
R2=int(input("Enter the number of rows for second matrix:\n"))

#main condition for matrix multiplication
if(C1!=R2):
    print("Invalid entry")
    exit()
C2=int(input("Enter the number of columns for second matrix:\n"))

#List comprehension for initialising all matrices elements to zero
a=[[0 for y in range(0,C1)]for x in range(0,R1)]
b=[[0 for y in range(0,C2)]for x in range(0,R2)]
c=[[0 for y in range(0,C2)]for x in range(0,R1)]

#function to print the matrix
def print_mat(matrix):
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            print(matrix[i][j],end=" ")
        print()

#function to perform matrix multiplication
def matrix_mul():
    for p in range(0,R1):
        for q in range(0,C1):
            a[p][q]=int(input("Enter an element:\n"))
    print("First matrix:\n")
    print_mat(a)

    for p in range(0,R2):
        for q in range(0,C2):
            b[p][q]=int(input("Enter an element:\n"))
    print("Second matrix:\n")
    print_mat(b)

    
    for p in range(0,R1):
        for q in range(0,C2):
            for r in range(0,R2):
                c[p][q]+=a[p][r]*b[r][q]

    print("The resultant matrix after multiplication is:\n")
    for i in range(0,R1):
        for j in range(0,C2):
            print(c[i][j],end=" ")
        print()

#calling the function
matrix_mul()
















