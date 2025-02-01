def isPossibleToSplit(nums) -> bool:
        my_dic = {}

        for num in nums:
            if num in my_dic:
                my_dic[num] += 1
                if my_dic[num] > 2:
                    return False
            else:
                my_dic[num] =1
        return True
