import random
import time
import concurrent.futures
start = time.perf_counter()
def comp1():
    count = 0
    for i in range(1,21):
        x = random.randrange(1,5)
        time.sleep(x)
        count += x
        print(f'In comp1, iteration no: {i}, time taken: {x}')
        
        
    return f'f1 completed with count {count}'      
def comp2():
    count = 0
    print("In comp2 before sleep")
    temp = random.randrange(5,10)
    time.sleep(temp)
    count +=temp
    print(f'In comp2 after 1st sleep, time: {temp}')
    temp = random.randrange(15,20)
    time.sleep(temp)
    count +=temp
    print(f'In comp2 after 2nd sleep, time: {temp}')
    
    return f"f2 completed with count: {count}"
    
with concurrent.futures.ThreadPoolExecutor() as executor:
    # TODO: write code...
    f1 = executor.submit(comp1)
    f2 = executor.submit(comp2)
    
    print(f1.result())
    print(f2.result())
    
finised = time.perf_counter()
temp = finised - start
print(f'Total time is {temp}')
    
