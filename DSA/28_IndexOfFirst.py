import re

class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        # Removes any non-alphanumeric characters
        pattern = re.escape(needle)

        # Matches the given pattern to the target string
        # Returns match object or none
        match = re.search(pattern, haystack)

        if match:
            return match.start()
        else: return -1

    
    def str(self, haystack: str, pattern: str) -> int:
        checking = True
        accumulator = []
        j = 1
        first_index = 0

        for i in range(len(haystack)):
            k = i

            if haystack[k] == pattern[0]:
                accumulator.append(haystack[k])
                #print(f"i,k,j{i,k,j}",accumulator)
                first_index = k
                while checking:
                    k =+1
                    j =+1
                    print(f"i,k,j{i,k,j}",accumulator)
                    if haystack[k] == pattern[j]:
                        accumulator.append(haystack[k])
                        print(accumulator)
                    else:
                        accumulator = []
                        checking = False
                        first_index = 0
            # if accumulator:
            #     return first_index
            # else:
            #     return -1



sol = Solution()
print(sol.str("fi","fi"))