'''
Greedy
    So who is better at each step
'''

from typing import List

def maxArea (heights: List[int]) -> int:

    i : int = 0
    j : int = len(heights) - 1

    max_left : int = 0
    max_right: int = 0
    max_area = float("-inf")

    while i <= j:
        if (j - i) * (heights[i]) * (heights[j]) > max_area:
            max_area = (j - i) * heights[i] if heights[i] < heights[j] else heights[j]
            
        if heights[i] > heights[max_left] and heights[j] > heights[max_right]:
            max_left = i
            max_right = j
        elif heights[i] > heights[max_left] and heights[j] <= heights[max_right]:
            max_left = i
        elif heights[i] <= heights[max_left] and heights[j] > heights[max_right]:
            max_right = j
        else:
            pass

        print(max_left, max_right, max_area)
        i += 1
        j -= 1
    
    return (max_right - max_left) * (heights[max_left]) * (heights[max_right])



def maxArea2 ( heights) -> int:

    i, j = 0, len(heights) - 1
    max_area = float('-inf')

    while i < j:
        smaller = min (heights[i], heights[j])
        max_area = max(max_area,  (j - i) * smaller)

        if heights[i] < heights[j]:
            i += 1
        else:
            j -= 1
    return max_area



print(maxArea2([1,8,6,2,5,4,8,3,7]))
