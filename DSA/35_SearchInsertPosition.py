import JSON_Loader as j
#data = json.load(r"C:\Users\Neamen\Documents\GitHub\Leetcode-Solutions\SearchInsertPosition.json")

json_data = j.JSON_Loader(r'C:\Users\Neamen\Documents\GitHub\Leetcode-Solutions\SearchInsertPosition.json')


class Solution:
    def searchInsert(self, nums, target):
        return self.Helper(nums, target, len(nums) - 1, 0)

    def Helper(self, nums, target, end, start):
        if start > end:
            return end + 1

        mid = (start + end) // 2

        difference = nums[mid] - target

        if difference == 0:
            return mid
        elif difference > 0:
            end = mid - 1
        else:
            start = mid + 1

        return self.Helper(nums, target, end, start)

instance = Solution()

# Allows for picking which test case to test
# Made to account for array indexing
test_case_number = -1
instance.searchInsert(json_data[test_case_number - 1]['nums'], json_data[test_case_number - 1]['target'])


# Test code on each test case
for case in json_data:
    print(f"Test case {case} ->" , "Result:", instance.searchInsert(
        case['nums'],case['target']
    ))



