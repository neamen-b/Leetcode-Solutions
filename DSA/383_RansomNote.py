
def canConstruct(ransomNote: str, magazine: str) -> bool:
        ranMap = {}
        magMap = {}

        for char in ransomNote:
            if char not in ranMap:
                ranMap[char] = 1
            else:
                ranMap[char] += 1

        for char in magazine:
            if char not in magMap:
                magMap[char] = 1
            else:
                magMap[char] += 1 

        for char in ransomNote:
            if char not in magMap or ranMap[char] > magMap[char]:
                return False

        return True