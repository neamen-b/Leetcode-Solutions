from collections import Counter

# This does not work because it does not guarantee the relative order of the elements
def isSubsequence(self, s: str, t: str) -> bool:
        scount = Counter(s)
        tcount = Counter(t)

        for key in scount.keys():
            if scount[key] != tcount[key]:
                return False
        
        # print(scount, tcount)
        for i in range(len(s)):
            boo = False

            for j in range(len(t)):
                if s[i] == t[j]:
                    boo = True
                if j == len(t) - 1 and boo == False:
                    return False
        return True

# Try a stack approach
# problem if s has same letters consecutively 
def issub(s, t):
     
    ans = []

    for i in range(len(s)):
          for j in range(len(t)):
            #    print(s[i], t[j])
               if s[i] == t[j]:
                    ans.append(t[j])
    print(ans)
    if s == "".join(ans):
         return True
    else:
         return False
    
# print(issub("acb","ahbgdc"))

# Let see if this work 

def issub2(s: str, t: str) -> bool:
     
    i : int = 0
    j : int = 0

    while i < len(s):
        # print(f"s = {s[i]}, t = {t[j]}, i = {i} , j = {j}")
        if j == len(t) and i < len(s):
               return False
          
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            j += 1
    return True

print(issub2(s = "axc", t = "ahbgdc"))