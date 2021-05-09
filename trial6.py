# file operations in python

# f = open('test.txt')
# Using open method
'''
# print(f.read()) #print all characters
# print(f.read(5)) #print first 5 characters

# print(f.readline())  # print first line
# print(f.readline())  # print second line

# Printing all lines at a time line by line

lines = f.readlines()
print(lines)  # All the lines in test.txt get stored in a list. The name of the list is lines

for l in lines:
    print(l)

line = f.readline()
while line != "":
    print(line)
    line = f.readline()

f.close()
'''

with open('test.txt', 'r') as f:
    lines = f.readlines()  # All the lines in test.txt will be stored in lines array
    reversed(lines)  # reverses order of lines in test.txt file
    with open('test1.txt', 'w') as f1:
        for i in reversed(lines):
            f1.write(i)
