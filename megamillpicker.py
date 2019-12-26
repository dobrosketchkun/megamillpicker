import quantumrandom
import time
import statistics
import random

import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)): 
    ssl._create_default_https_context = ssl._create_unverified_context

BIG = 71
SMALL = 26

print("Receiving quantum randomness...")
time1 = time.time()
quarray = []
for _i in range(10):
	time0 = time.time()
	quarray += quantumrandom.get_data(data_type='uint16', array_length=1000)
	print('*'*random.randint(1,20))
	#print('time', time.time()-time0)
#print('time_all', time.time()-time1)
def first():
		rand = [x%BIG for x in quarray]
		num = [x for x in range(1,BIG)]
		cou = [(_i,rand.count(_i)) for _i in num]
		#print('cou', cou)
		mean = statistics.mean([x for (i,x) in cou])
		#print('mean', mean)
		divi = [((_n - mean), _i) for (_i,_n) in cou]
		#print(divi)
		maxes = []
		sort = [(x,y) for (y,x) in sorted(divi)]
		#print('sort',sort)
		return sort[0:5], sort[::-1][0:5]

def second():
		rand = [x%SMALL for x in quarray]
		#print(rand)
		num = [x for x in range(1,SMALL)]
		cou = [(_i,rand.count(_i)) for _i in num]
		#print('cou', cou)
		mean = statistics.mean([x for (i,x) in cou])
		#print('mean', mean)
		divi = [((_n - mean), _i) for (_i,_n) in cou]
		#print(divi)
		maxes = []
		sort = [(x,y) for (y,x) in sorted(divi)]
		#print('sort',sort)
		return sort[0:1], sort[::-1][0:1]

f70 = first()
s25 = second()

# print(f70[0], s25[0])
# minus = [x for (x,y) in f70[0]], [x for (x,y) in s25[0]]
# print(minus)
# print(f70[1], s25[1])


plus = [x for (x,y) in f70[1]], [x for (x,y) in s25[1]]
a,b,c,d,e = plus[0]
f = plus[1][0]
print('Your numbers are ' + str(a) +', ' + str(b) +', ' + str(c) +', ' + str(d) +', ' + str(e)  +' and ' + str(f)) 
