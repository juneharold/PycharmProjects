import time
start_time = time.time()

a=[x for x in range(10**8)]
sum=0
for i in a:
    sum+=i

print("--- %s seconds ---" % (time.time() - start_time))