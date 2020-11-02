import time

#HW5 question 1: Optimize this code
i=0
start_time1 = time.time()
while i<100:
    item = 10
    i=i+item
print("--- %s seconds for initial program---" % (time.time() - start_time1))

#beginning optimized code
i=0
start_time2 = time.time()
item = 10
while i<100:
    i=i+item
print("--- %s seconds for optimized program---" % (time.time() - start_time2))

#optimized program runs about 1(10^-6) seconds faster (approximately 30% faster on my machine)