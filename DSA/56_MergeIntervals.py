'''
Check if the the first element of the range 1 index ahead of the current one is less than the upper of the current

'''

def merge(intervals):
    ans = []
    i = 0
    while i < len(intervals):
        # print(f"i = {i}, checking {intervals[i]}")

        # If so, they over lap
        if i < len(intervals)-1 and intervals[i+1][0] <= intervals[i][1]:
            # print([intervals[i][0],intervals[i+1][1]])
            if intervals[i+1][0] < intervals[i][0]:
                ans.append([intervals[i+1][0], intervals[i+1][1]])
            else:
                ans.append([intervals[i][0],intervals[i+1][1]])
            # If you merge, skip the merged
            i+=1
        else:
            ans.append(intervals[i])
        i += 1
    print(ans)

merge([[1,4],[0,4]])

# l1 = []
# l1.append([1,2])
# print(l1)