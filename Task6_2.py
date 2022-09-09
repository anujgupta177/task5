import random
import time
import concurrent.futures

start = time.perf_counter()
process = []
def comp1():
    count = 0
    for i in range(1,21):
        x = random.randrange(1,5)
        time.sleep(x)
        count += x
        print(f'In "comp_1" iteration no: {i}, time taken: {x}')
        
    return f'f1 completed with count: {count}'   
    
    
    
with concurrent.futures.ThreadPoolExecutor() as executor:
    # TODO: write code...
    f1 = executor.submit(comp1)
    print(f1.result())
    
    
finised = time.perf_counter()
temp = finised - start
print(f'Total time is {temp}')
    
