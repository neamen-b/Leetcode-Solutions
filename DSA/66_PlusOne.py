from typing import List
class Solution:

    def plusOne(self, digits: List[int]) -> List[int]:
        st = [str(x) for x in digits]
        (print(st))
        st_num = ''.join(st)
        (print(st_num))

        num = int(st_num)
        (print(num, type(num)))
        num += 1
        (print("sum",num))

        st_num = str(num)
        (print(st_num))
        int_list = []
        for s in st_num:
            print(s)
            int_list.append(int(s))

        return int_list
    
sol = Solution()
print(sol.plusOne([9]))