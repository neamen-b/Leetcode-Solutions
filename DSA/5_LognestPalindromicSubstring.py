'''
can only think of an O(n^2) solution right now

check for all subtrings
check if those substrings are palindromic:
    if so:
        find the longest one by changing it everytime you go through

'''
# Way too slow
def longestPalindrome(s):

    sub_strings = []

    if len(s) == 0:
        return ''
    
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub_strings.append(s[i:j+1])

    largest_Sub_string = ''

    for string in sub_strings:
        if string[::-1] == string and len(string) > len(largest_Sub_string):
            largest_Sub_string = string
    return largest_Sub_string

print(longestPalindrome('cbbd'))

