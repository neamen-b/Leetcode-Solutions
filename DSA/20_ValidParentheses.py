
class Solution:
    def isValid(self, s: str) -> bool:

        # Stack to keep track of parenthesis
        # FILO
        stack = []

        # Using sets because of O(1) lookup
        # Which doesn't really much considering the size of the sets
        # Set for opening parentheses
        open = {'[','{','('}

        # Set for closing parentheses
        close = {']','}',')'}

        mydic = {
            "[" : "]",
            "{" : "}",
            "(" : ")"
        }

        for char in s:

            if char in open:
                stack.append(char)
            
            elif char in close:
                
                # print(f"mydic @ {mydic[stack[len(stack)-1]]}")
                # print(f"stack @ {stack[len(stack)-1]}")
                
                if not stack or mydic[stack[-1]] != char:
                    return False
                
                stack.pop()
        
        return not stack
                # current = stack.pop()
                # if mydic[current] == char:
                    
sol = Solution()
print(sol.isValid("()"))

