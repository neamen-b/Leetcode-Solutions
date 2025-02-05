class Solution:
    def countCharacters(words, chars: str) -> int:
        
        def check(candidate, source):
            sourceMap = {}
            for char in source:
                if char in sourceMap:
                    sourceMap[char] += 1
                else:
                    sourceMap[char] = 1
            
            for char in candidate:
                if char not in sourceMap or sourceMap[char] <= 0:
                    return 0
                sourceMap[char] -= 1
            return len(candidate)

        sum = 0
        for word in words:
            sum += check(word, chars)
        return sum