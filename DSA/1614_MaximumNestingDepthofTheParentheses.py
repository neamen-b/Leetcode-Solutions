def maxDepth(self, s: str) -> int:
        count = 0
        max_v = -1

        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                if count > max_v:
                    max_v = count
                count -= 1
            else:
                pass
        
        # If there are no parenthesis
        if max_v == -1:
            return 0
        return max_v
        