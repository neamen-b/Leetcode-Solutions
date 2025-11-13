from typing import List, Tuple


class Solution:
    def reverseStr(self, s : str, k : int) -> str:
        word = [char for char in s]

        print(f"word {word} {type(word)}")
        group_end = 2 * k - 1
        group_start = 0
        num_of_substrings = len(s) // (2 * k)
        remain = len(s) % (2 * k)
        ans = ""
        for i in range(1, num_of_substrings + 1):
            # print(group_start, group_end)
            ans += self.reverse(word[group_start : group_start + k])
            ans += ''.join(word[group_start + k : group_end + 1])
            group_start += 2 * k
            group_end += 2 * k
        
        if remain >= k:
            ans += self.reverse(word[group_start : group_start + k])
            ans += ''.join(word[group_start + k : group_end + 1])
        else:
            ans += ''.join(word[group_start :])

        return ans


    def reverseStr2 (self, s : str, k : int) -> str:
        word = [char for char in s]
        start = 0
        end = start + k - 1
        group_end = 2 * k - 1

        
        while end < len(word):
            print(start, end, group_end, word)
            self.reverse(word, start, end)
            start += group_end + 1
            end = start + k - 1
            group_end += (2 * k) -1

        if k >= len(word):
            self.reverse(word, 0, len(word) - 1)
            return "".join(word)
        
        # print(f"word {word}")
        return "".join(word)


    def reverse(self, word : List[str], start : int, end : int) -> None:
        while start < end:
            word[start], word[end] = word[end], word[start]
            start += 1
            end -= 1


def test(words : List[Tuple[str, int]]):
    obj = Solution()
    for word, k in words:
        print(obj.reverseStr2(word, k))

words = [("abcdefg", 2), ("abcd", 3), ("", 1), ("a", 2), ("abcdefg", 8)]

test(words)

