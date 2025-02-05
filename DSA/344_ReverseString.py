'''
Initial thoghts
    This is an in place reverse
    Two pointer method

    step 1
        Defined two pointers.
        O(1) space complexity
        start, end = 0, len(s) -1

    step 2
        swap values at opposite end, the middle values stays there
        O(n/2) where n is len(s) which is O(n) amortized
        while start < end:
            s[start], s[end] = s[end], s[start]


'''

class Solution:

    def reverseString(s: str) -> None:

        start = 0
        end = len(s) - 1
        # This would work even if <=, it would just swap the middle element with itself
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

test = ["h", "e", "l", "l", " ", "o"]
print(test[:])
Solution.reverseString(test)