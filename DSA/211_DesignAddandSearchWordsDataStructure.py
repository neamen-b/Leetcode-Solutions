'''
A trie with the search function switched up
'''
from typing import List, Callable
class TreeNode:
    def __init__ (self):
        self.children = dict()
        self.isEndofWord = False
        self.letter = ''
        # # You don't need this because the words to be insreted will not have dots
        # self.isDot = False

class Dictionary:
    def __init__(self):
        self.root = TreeNode()
    
    def addWord(self, word : str) -> None:
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TreeNode()
            
            current_node = current_node.children[char]
            current_node.letter = char
        current_node.isEndofWord = True
    
    def dfs (self, node : TreeNode) -> set:
        stack = [(node, node.letter)]
        words = set()

        while stack:
            # print(f"stack : {stack}")
            curr , char = stack.pop()
            if curr.isEndofWord == True:
                words.add(char)
            
            for key, treenode in sorted(curr.children.items()):
                stack.append((treenode, char + key))
        # print(f"here {node.letter} , words : {words}")
        return words

    def matchPattern(self, word :str, pattern : str) -> bool:
        if len(word) != len(pattern):
            return False

        for word_char, pattern_char in zip(word, pattern):
            if pattern_char != '.' and word_char != pattern_char:
                return False
        return True
            
            
    def search (self, word : str) -> bool:
        # match is exactly the same. Fair assumption
        current_node = self.root

        for char in word:
            if char == ".":
                # print(f"search {word} at {char}")
                words = self.dfs(current_node)
            
                for w in words:
                    if self.matchPattern(w, word):
                        return True
                return False

            if char not in current_node.children:
                    return False
            current_node = current_node.children[char]
        
        if current_node.isEndofWord == True:
            return True
        else:
            False


words = ['bdm', 'bad', 'dad', 'mad', 'pad', 'bad', '.ad', 'b..', '...']
obj = Dictionary()
functions = [obj.add, obj.add, obj.add, obj.add, obj.search, obj.search, obj.search, obj.search, obj.search]

def testDictionary(words : List[str], functions = List[Callable]) -> None:

    for i in range(len(words)):
        print(functions[i](words[i]))

testDictionary(words, functions)
