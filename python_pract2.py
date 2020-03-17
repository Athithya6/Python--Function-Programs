#filename='Athithya2.txt'
#with open(filename,'w') as f:
    #f.write("A boy's best friend is his mother.")
#with open(filename,'a') as f:
 #   f.write("\nHere's looking at you kid.\n All right Mr.DeMille, I am ready for "
  # "  my closeup.\n I would not join any club that would have me as its "
  # " member")

#with open(filename,'r') as f:
 #  lines= f.readlines()
#for i in lines:
 #   print(i)


'''
with open(filename,'a') as f:
    f.write("\n This list is life.This list is absolute good."
            "\n Funny how?Funny like a clown?")
'''

#f=open('Athithya1.txt','r')
#for c in f:
   # print(c)

#f=open('Athithya2.txt','r')
#print(f.read())
#print f.read(20)

#g=open('Athi.txt','r')
#print g.readline()
#print g.readlines()
#g.close()

#k=open('Athithya3.txt','w')
#k.write('I am doing the write operation now')
#k.write('\n It can be used to create a new file and write into it')
#k.write('\n It can also be used to overwrite in an existing file.')
#k.close()

'''
l=open('Athithya3.txt','a')
l.write('\nThis is the append operation')
l.write('\nIt can be used to add text at the end of an article')
l.close()
'''

#m=open('Athithya4.txt','w')
#m.write('This is a trial file. I will delete it soon')
#m.close()

#n=open('Athithya5.txt','w')
#n.write('This is also a trial file. I will delete it soon')
#n.close()

#import os
#os.remove('Athithya4.txt')

#import os
#if os.path.exists('Athithya5.txt'):
 #   os.remove('Athithya5.txt')
#else:
 #   print('This file does not exist')

#import os
#os.rmdir('Athithya1')

#f=open('python_pract.py','rb')
#f.close()

'''
f=open('Athithya1.txt','rb')
print("Name of the file: ",f.name)
print("Mode of file: ",f.mode)
print("Closed or not: ",f.closed)

print(f.readline())
f.close()


print("Closed or not: ",f.closed)
'''

'''
fo=open('Athithya1.txt','r+')
str=fo.read(20)
print("The string is :",str)
'''

'''
position =fo.tell()
print("Position: ",position)
'''

'''
new_pos=fo.seek(0,0)
print("New position is: ",new_pos)
'''

'''
f=open('Athithya1.bin','wb')
arr=[1,2,3,4]
arrb=bytearray(arr)
f.write(arrb)
f.close()
'''

'''
f=open('Athithya1.bin','rb')
num=list(f.read())
print(num)
f.close()
'''

#f=open('Aparna.txt','w')
#f.write('I am Aparna \n I am from kerala \n I am feeling better now')

'''
#f=open('Aparna.txt','r')
#print(f.read())
#print(f.readline())
#print(f.readlines())
#count=0
f= open('Athithya1.txt','r')
#for i in f:
 #   count+=1
#print("Total no.of lines: ",count)
all_lines=f.readlines()
for i in range(0,3):
    print(all_lines[i])
'''

f=open('lotus.jpeg','rb')
f1=open('lotus2.jpeg','wb')
for i in f:
   f1.write(i) 

