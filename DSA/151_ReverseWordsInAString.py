'''
split
reverse
add to ans if not space

'''

def reverseWords(s):
    words = s.split()
    ans = ""
    for i in range(len(words) -1, -1, -1):
        if words[i] != " ":
            if i == 0:
                ans += f"{words[i]}"
            else:
                ans += f"{words[i]} "
    return ans

print(reverseWords("  a  "))
