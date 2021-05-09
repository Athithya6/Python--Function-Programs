# List comprehensions and while loop

# Celsius to fahrenheit using ordinary for loop
'''
celsius = [12.5, 36.6, 37, 43, 49]
fahrenheit = []

for i in celsius:
    caltemp = (((9 / 5) * i) + 32)
    fahrenheit.append(caltemp)
print("Input Celsius tempertures in fahrenheit: ", fahrenheit)
'''

'''
# Celsius to fahrenheit using list comprehension
c = [12.5, 36, 6, 37, 43, 49]
f = [((9 / 5) * i) + 32 for i in c]

print(f)
'''

'''
result = ["MULTIPLE OF 3" if x % 3 == 0 else "NON-MULTIPLE OF 3" for x in range(1, 20)]
print(result)

x = [i*j for i in range(1, 10) for j in range(1, 6)]
print (x)
'''

# while loop
'''
k=5

while(k>0):
    print(k)
    k-=1
    if(k==2):
        continue

print("while loop execution complete")
'''

k=10

while(k>1):
    if(k==8):
        k-=1
        continue

    if(k==1):
        break
    print(k)
    k-=1
