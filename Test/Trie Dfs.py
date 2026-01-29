'''
Dfsing a trie

'''
from typing import List
class TreeNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
        self.letter = ""


class Trie:
    def __init__ (self):
        self.root = TreeNode()
    def insert(self, word : str):
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TreeNode()
            current = current.children[char]
            current.letter = char
        current.isEndOfWord =True

    def dfs(self, start) -> List[str]:
        stack = [(start, start.letter)]
        words = []
        print(f"root: {self.root}")
        while stack:
            print("stack", stack)
            curr, char = stack.pop()

            if curr.isEndOfWord:
                words.append(char)
                
            
            for key, child in sorted(curr.children.items()):
                stack.append((child, char + key))
        return words


words : List[str] = [ 
    "apple", "app", "cool", "cook"
]

obj = Trie()

def testInsert (object : Trie , words : List[str]) -> None:
    
    for word in words:
        object.insert(word)

def testDfs (object : Trie) -> None:
    print(obj.dfs(obj.root))

testInsert(obj, words)
testDfs(obj)





