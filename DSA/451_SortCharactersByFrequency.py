'''
Initial thoughts:

    First get the frequency of each char in s
    Then add these characters to a new string in decreasing order of frequency

        Now I can just add (frequency, index) tuples to a list and sort by frequency)

        then loop over it, accessing each tuple and adding the letter s[index] frequency times

        Sorting would make this solution O(n logn)

    I can also heapify and just pop from the max heap to do the same thing.

        Also O(nlogn) solution as heapify() is O(n) and pop() is O(log n). 
        I'll need to pop n times. 
        Basically a heapsort

'''

import heapq
import time
# heap approach
def frequency_sort(s : str)-> str:
    mymap = {}
    ans = []
    tuples = []

    # Frequency tables using a dictionary
    for i in range(len(s)):
        if s[i] in mymap:
            mymap[s[i]] += 1
        else:
            mymap[s[i]] = 1
    
    #Problem here is that I want to sort by values, not keys

    # this could be problematic because s can have 2 chars with freq = 2
    # and map keys have to be unique
    # you don't need to change the og dictionary, just the reverse a tuples to a list
    # Making value negative since python heapify is minheap only
    for key, value in mymap.items():
        tuples.append((-value, key))
    
    # now heapify
    heapq.heapify(tuples)

    for i in range(len(tuples)):
        tup = heapq.heappop(tuples)
        freq = abs(tup[0])
        chr = tup[1]
        ans.append(chr * freq)

    return ''.join(ans)
start = time.time()
print(frequency_sort("tree"))
end = time.time()
print(end - start)

# Sort attempt
def frequency_sort2(s:str) -> str:
    mymap = {}
    ans = []
    tuples = []

    # Frequency tables using a dictionary
    for i in range(len(s)):
        if s[i] in mymap:
            mymap[s[i]] += 1
        else:
            mymap[s[i]] = 1
    
    #Problem here is that I want to sort by values, not keys

    # this could be problematic because s can have 2 chars with freq = 2
    # and map keys have to be unique
    # you don't need to change the og dictionary, just the reverse a tuples to a list
    # Making value negative since python heapify is minheap only
    for key, value in mymap.items():
        tuples.append((value, key))
    
    # now sort
    tuples.sort(reverse=True)
    print(tuples)

    for i in range(len(tuples)):
        tup = tuples[i]
        freq = abs(tup[0])
        chr = tup[1]
        ans.append(chr * freq)

    return ''.join(ans)

start = time.time()
print(frequency_sort2("tree"))
end = time.time()
print(end - start)
# print(frequency_sort2('tree'))

