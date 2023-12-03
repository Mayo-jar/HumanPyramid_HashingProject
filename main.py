# import whatever you need here
import time
import sys
from hashmap import HashMap
func_calls = 0
cache_hits = 0

# Part 1 -- Write weight_on_cacheless() method
def weight_on_cacheless(r,c):
    if r == 0 and c == 0:
        return 0.00
    
    elif c == 0:
        return 0.5 * (200.00 + weight_on_cacheless(r-1,c))
    
    elif c==r:
        return 0.5 * (200.00 + weight_on_cacheless(r-1,c-1))
    
    return 0.5 * (400.00 + weight_on_cacheless(r-1,c-1) + weight_on_cacheless(r-1,c))

# Part 3 -- Write weight_on_with_caching() method

def weight_on_with_caching(r,c,cache):
    global func_calls
    global cache_hits

    if (r,c) in cache.keys():
        cache_hits += 1
        return cache.get((r,c))
    else:
        if r == 0:
            return cache.set((r,c),0.00)
        
        elif c == 0:
            func_calls += 1
            return cache.set((r,c), 0.5 * (200.00 + weight_on_with_caching(r-1,c,cache)))
        
        elif c==r:
            func_calls += 1
            return cache.set((r,c), 0.5 * (200.00 + weight_on_with_caching(r-1,c-1,cache)))
        
        func_calls += 2
        return cache.set((r,c), 0.5 * (400.00 + weight_on_with_caching(r-1,c-1,cache) + weight_on_with_caching(r-1,c,cache)))
    
def main():
    # Part 2 -- Use weight_on_cacheless() method
    # Cacheless
    print("Cacheless:")
    start = time.perf_counter()
    i = 0
    #num = int(sys.argv[1])
    num = 7
    f = open("cacheless.txt","w")
    while i < num:
        j = 0
        row = ""
        while j <= i:
            row += '{:.2f}'.format((weight_on_cacheless(i,j))) + " "
            j+=1
        print(row)
        f.write(row + '\n')
        i+=1
    elapsed = time.perf_counter() - start
    print("\nElapsed time: " + str(elapsed) + " seconds.")
    f.write("\nElapsed time: " + str(elapsed) + " seconds." + '\n')
    f.close()
    
    # Part 3 -- Use weight_on_with_caching() method, with your HashMap ADT
    
    print("With Caching:")
    i = 0
    cache = HashMap()
    global func_calls
    start = time.perf_counter()
    f = open("with_caching.txt","w")
    while i < num:
        j = 0
        row = ""
        while j <= i:
            row += '{:.2f}'.format((weight_on_with_caching(i,j,cache))) + " "
            func_calls += 1
            j+=1
        print(row)
        f.write(row + '\n')
        i+=1
    elapsed = time.perf_counter() - start
    print("\nElapsed time: " + str(elapsed) + " seconds.")
    f.write("\nElapsed time: " + str(elapsed) + " seconds." + '\n')
    
    print("Number of function calls: " + str(func_calls))
    print("Number of cache hits: " + str(cache_hits))

    f.close()
    
if __name__=="__main__":
    main()

