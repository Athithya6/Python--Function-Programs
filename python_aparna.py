#array in python
'''
import  array as arr
a=arr.array('i',[1,2,3,4,2,5])
print("the array is",end=' ')
for i in range(0,len(a)):
    print(a[i])

#inserting elements

a.insert(2,11)
print('\n The new array is')
for i in range(0,len(a)):
    print(a[i],end=' ')
a.append(17)
print("\n again the new array is :",end=' ')
for i in range(0,len(a)):
    print(a[i],end=' ')

#removing elements

a.pop(3)
a.remove(2)
print('\n the array after removal is',end=' ')
for i in range(0,len(a)):
    print(a[i],end=' ')


#searching element

print("\n the ocurence of 4:",end=' ')
print(a.index(4))
'''

from numpy import *

arr1= array([

     [1,2,3],
     [4,5,6]


    ])
#print(arr1.ndim)       #No.of dimensions
#print(arr1.shape)      #No.of rows and columns
#print(arr1.size)       #Size

