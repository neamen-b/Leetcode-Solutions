class Solution:
    def finalString(self, s: str) -> str:
        
        ans = []
        for char in s:
            if char == 'i':
                ans.reverse()
            else:
                ans.append(char)
        return ''.join(ans)
