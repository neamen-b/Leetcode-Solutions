'''
initial thoughts - 
    step 1 - determining if a character in s is a vowel or not
        implement a hashset initialized to the vowel characters. Use this for constant lookup. 
                if char in set:
                    then vowel
                else:
                    consonant
    step 2 - 
        To avoid using the index() funciton, which is O(n) worst case, implement a hashmap of vowel to index
        you'll need this for look up of insertion point. No.. forget this

    step 3 - 
        I know where the consonants are going to go, s[i] goes to t[i]
        vowels:
            find the ASCII value for each vowel
            add it to an array and then sort
            use this array to populate the new string

    step 4 - 
        Initialize an empty array where each element is initially ""
            while performing step 1, add consonant at corresponding i

        vowels_counter = 0
        for i in range(length(s)):
            i arr[i] == "":
                arr[i] = vowels[vowels_counter]
                vowels_counter += 1
        return ''.join(arr)


        Order:
            sort makes in nlogn

    step 5 - 
        optimization

        can't do much about time but I can improve on space use. for example I don't need a new array
        to store the result. I can judt edit s (given i don't care about keeping s)

'''


def sortVowels(s):
    # Special case
    if len(s) == 1:
        return s
    
    #Vowels container. Set() can take an iterable such as a list
    vowels = set(['A', 'E', 'I', 'O', 'U', 'a', 'i', 'e', 'o', 'u'])

    # Answer. Using list comprehension to populate with ""
    ans_str = [' ' for _ in range(len(s))]

    vowels_sort = []
    # This handles 
    for i in range(len(s)):
        if s[i] not in vowels:
            # print(f"cons at {i},type of index {type(i)}, {s[i]}")
            # Insert consonant at the same index in ans
            ans_str[i] = s[i]
        else:
            # Append tuple (ASCII val of char, char)
            vowels_sort.append((ord(s[i]), s[i]))
    # print(f"ans after cons {ans_str}")

    # This sorts the list by the first element in the tuple. Automatically non-decresing.
    # .sort() would have done the same i think where it sorts by the first element of the tuples
    vowels_sort.sort(key=lambda x : x[0])
    # print(vowels_sort)
    vowel_count = 0

    for i in range(len(ans_str)):
        # If the rest are consonants break 
        if vowel_count > len(vowels_sort): break
        # if not already consonant
        if ans_str[i] == ' ':
            # assign this space to the smallest ascii vowel
            # acess tuples with vowel count. char is at tuple[1]
            # print(vowel_count)
            ans_str[i] = vowels_sort[vowel_count][1]
            vowel_count += 1
    
    return ''.join(ans_str)

# print(sortVowels("lYmpH"))

# This does not work because you cannot mutate strings
def sortVowels2(s):
    # Special case
    if len(s) == 1:
        return s
    
    #Vowels container. Set() can take an iterable such as a list
    vowels = set(['A', 'E', 'I', 'O', 'U', 'a', 'i', 'e', 'o', 'u'])
    vowels_sort = []
    # This handles 
    for i in range(len(s)):
        if s[i] in vowels:
            # Append tuple (ASCII val of char, char)
            vowels_sort.append((ord(s[i]), s[i]))

    # This sorts the list by the first element in the tuple. Automatically non-decresing.
    # .sort() would have done the same i think where it sorts by the first element of the tuples
    vowels_sort.sort(key=lambda x : x[0])
    # print(vowels_sort)
    vowel_count = 0

    for i in range(len(s)):
        # If the rest are consonants break 
        if vowel_count > len(vowels_sort): break

        if s[i] in vowels:
            s[i] = vowels_sort[vowel_count][1]
            vowel_count += 1
    return s

print(sortVowels2("lEetcOde"))

def learn():
    l = [(1,'b'), (1, 'a'), (-4,'g')]

    print(l)
    # No key defintion. Automatically by the first element 
    # l.sort()
    #output  = [(-4, 'g'), (1, 'b'), (1, 'a')]

    # explicitly by the first element
    # l.sort(key= lambda x : x[0])
    #output = [(-4, 'g'), (1, 'b'), (1, 'a')]

    # explicityly by the first element but ties are broken by looking at the second element
    # Sort by x[0], if ties, resort to x[1]
    #output = [(-4, 'g'), (1, 'a'), (1, 'b')]
    l.sort(key = lambda x : (x[0], x[1]))

    print(l)

# print('help')
# learn()
    



