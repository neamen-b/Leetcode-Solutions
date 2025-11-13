from typing import List


# Works but is too slow
def distance (nums: List[int]) -> int:
        my_map = {}

        for i in range(len(nums)):

            if nums[i] in my_map:
                my_map[nums[i]].append(i)
            else:
                my_map[nums[i]] = [i]
        # print(seen)
        # print(my_map)

        ans = []

        for i in range(len(nums)):
            sumind = 0
            for j in my_map[nums[i]]:
                print(nums[i], j)
                if j != i:
                    sumind += abs(i - j)
            ans.append(sumind)
        print(ans)

        return ans

# distance([1,3,1,1,2]) 

#Second attempt. Optimized
def distance2 (nums: List[int]) -> int:
        my_map = {}

        for i in range(len(nums)):

            if nums[i] in my_map:
                my_map[nums[i]][0].append(i)
                my_map[nums[i]][1][0] += i
            else:
                my_map[nums[i]] = [[i],[i]]
        # print(seen)
        print(my_map)

        ans = []

        for i in range(len(nums)):
            size = len(my_map[nums[i]][0])
            print(size)
            ans.append( abs ( my_map[nums[i]][1][0] - i * size))
        print(ans)

        return ans
distance2([1,3,1,1,2])

# 0 1 2 3 4 
# 1 3 1 1 2

# index 3
# 3 - 3 + 2 - 3 + 0 - 3 = 3 + 2 + 0 - 3 - 3 - 3 = 5 - 9 = -4

#index 2
# 3 - 2 + 2 - 2 + 0 - 2 = 3 + 2 + 0 - 2 - 2 - 2 = 5 - 6 = -1
# 2 - 3 + 2 - 2 + 2 - 0 = 2 + 2 + 2 - 3 - 2 = 6 - 5 = 1  