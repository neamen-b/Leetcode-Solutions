class Solution:
    # Dictionary to store calculated values
    mydic = {}
    def climbStairs(self, n: int) -> int:
        
        # If it's already calculated, just access it from the dictionary
        if n in Solution.mydic:
            return Solution.mydic[n]

        # Base cases
        if n==0:
            return 0
        
        if n==1:
            return 1

        if n==2:
            return 2

        # If not in already, add it for next time
        Solution.mydic[n] = self.climbStairs( n-1) + self.climbStairs( n-2)
        return Solution.mydic[n]