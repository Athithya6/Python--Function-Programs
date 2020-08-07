#Collections module
#Counter

'''
from collections import Counter

print(dir(Counter))

mylist1 = [1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,7,7,7,7,7,7,7,7,7]
print(Counter(mylist1))

mylist2=['Amma','Aishwar','Paati','Athithya','Daddy','Paati','Amma','Amma','Aishwar','Amma','Amma','Athithya','Daddy','Daddy','Athithya','Paati','Amma','Aishwar','Aishwar','Athithya','Amma','Athithya','Amma','Aishwar','Athithya','Paati','Paati','Paati','Daddy','Daddy','Paati','Daddy','Aishwar','Amma','Athithya']
print(Counter(mylist2))

mylist3=['Steven','Spielberg',1993,72,7,7,72,'Spielberg','Williams','Zaillian',1993,7,72,'Kingsley','Neeson','Fiennes','Kingsley','Steven',72,1993]
print(Counter(mylist3))

d=Counter(mylist3)
print(type(d))

print(Counter("Peter Piper picked a peck of pickled pipers.Betty Botter bought some butter but buttered the butter on her butt so that her butt became buttery."))

sentence = "She sells seashells by the seashore and how can a clam cram in a clean cream can?"
print(Counter(sentence.split()))

letters = 'cwhdvceugbcfjvcbfhdgvcwmjkhcsdcpwoerpwepujigyhfxsdfvqwfrtwddjvcnshgcjfehvkuhvukgjybvyjvbfhdjkshdjgchsgvcjhsgcfvpfpeoruutyrjeghfjsdvncbmnxbmcxbnxvcznbvcshgcwuhicwpedpwru'
c= Counter(letters)
print(c.most_common())
print(list(c))
'''

'''
from collections import defaultdict

d={'a':10,'b':20,'c':30}
print(d['c'])
print(d['god'])   #returns error as there is no key named 'god'


e = defaultdict(lambda:0)
e['correct']=50
print(e['wrong'])
print(e)
'''

'''
from collections import namedtuple
Dog = namedtuple('Dog',['age','breed','name'])
herc = Dog(age=5,breed='poodle',name='Hercules')
print(type(herc))
print(herc)
print(herc.age)
print(herc.breed)
print(herc.name)
print(herc[1])
'''

'''
#datetime module

import datetime


mytime = datetime.time(16,45,32,22)
print(mytime.hour)
print(mytime.minute)
print(mytime.second)
print(mytime.microsecond)
print(mytime)
print(mytime.tzinfo)
print(mytime.isoformat())
print(mytime.tzname())



today = datetime.date.today()
print(today)
print(today.year)
print(today.month)
print(today.weekday())
print(today.day)
print(today.ctime())
'''


#timing a python code
import time
def func_one(n):
	return [str(num) for num in range(n)]

result1 = func_one(20)
#print(result1)

def func_two(n):
	return list(map(str,range(n)))

result2 = func_two(20)
#print(result2)

'''
start_time1 = time.time()

result= func_one(10000)

end_time1 = time.time()

elapse_time1 = end_time1 - start_time1
print(elapse_time1)


start_time2 = time.time()

result = func_two(10000)

end_time2 = time.time()

elapse_time2 = end_time2 - start_time2
print(elapse_time2)
'''

'''
#using timeit module
import timeit


stmt1 = '''
func_one(100)
'''

setup1 = '''
def func_one(n):
	return [str(num) for num in range(n)]
'''

print(timeit.timeit(stmt1,setup1,number=1000000))

stmt2 = '''
func_two(100)
'''

setup2 = '''
def func_two(n):
	return list(map(str,range(n)))
'''
print(timeit.timeit(stmt2,setup2,number=1000000))
'''

#RegEx
import re
'''
text= "Hi I am Athithya. My number is 444-555-6666."
phone = re.search(r"\d{3}-\d{3}-\d{4}",text)
print(phone)

phone_pattern = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
results = re.search(phone_pattern,text)
print(results.group())
print(results.group(2))
print(results.group(5))
'''

string = "aaaaaaTTTTT444499DHJKKKKKLAXC22776618340000777888000GHJcvv  vvvbbqqllooAZX"
pat_one = re.search(r"\w{3,}",string)
pat_two = re.search(r"\W{4}",string)
pat_three = re.search(r"D\D\D",string)
pat_four = re.search(r"\d{4,6}",string)
part_five = re.search(r"\S*",string)
part_six = re.search(r"\s?",string)
print(pat_one)
print(pat_two)
print(pat_three)
print(pat_four)
print(part_five)
print(part_six)





