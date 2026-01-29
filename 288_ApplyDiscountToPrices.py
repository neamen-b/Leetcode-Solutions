# Python my love, ket's do this

class Solution:

    def discountPrices(self, string : str, discount : int) -> str:
        words = string.split(" ")
        new_words = []
        num = 0
        for word in words:
            if word[0] == "$" and word[1:].isdigit():
                num = float(word[1:])
                num = num * (1-(discount / 100.0))
                new_words.append("${:.2f}".format(num))
            else:
                new_words.append(word)
        
        return ' '.join(new_words)

sol = Solution()
ans = sol.discountPrices("But me $10 and then buy $20", 50)
print(ans)
    