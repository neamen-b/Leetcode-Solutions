from collections import Counter


s = "test"

# sCounter = Counter(s)
# print(sCounter)
def rearrangeCharacters(s:str , target: str):
    sCount = Counter(s)
    tCount = Counter(target)

    count = []

    for char in target:
        count.append(sCount[char] // tCount[char])
    print(count)
    print(min(count))
    return min(count)

rearrangeCharacters("abcba","abbcba")

'''
Tries to imporove space complexity by not using the count list but not that much faster. 
According to leetcode at least. 
'''

def rearrangeCharacters(s: str, target: str) -> int:
        sCount = Counter(s)
        tCount = Counter(target)
        count = float('inf')

        for char in target:
            ratio = (sCount[char] // tCount[char])
            if ratio < count:
                count = ratio
        return count 