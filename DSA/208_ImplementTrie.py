'''
A trie is a tree where one node can have more than two children
Used for autocompletion 

The implementation below is for strings of ONLY lowercase alphabet characters. children <= 26
If uppercase children are included, children <= 52
If digits are included, children <= 61

The root node is empty. Has 26 children 
'''


from typing import List, Optional, Callable

class Node:
    def __init__ (self) -> None:
        # Each node can have 26 children. a-z
        self.children = {}
        # Each node can be the end of a word. This flag indicates
        self.isEndOfWord = False


class Trie:

    def __init__ (self) -> None:
        # The root of the Trie. 
        self.root = Node()
    
    def insert (self, word  : str) -> str:
        current_node = self.root

        for chr in word:
            if chr not in current_node.children:
                new_node = Node()
                current_node.children[chr] = new_node
            current_node = current_node.children[chr]
        current_node.isEndOfWord = True
        return f"{word} added successfully."

    
    def search(self, word :str) -> bool:
        current_node = self.root

        for chr in word:
            if chr not in current_node.children:
                return False
            current_node = current_node.children[chr]
        
        # This might be overkill. 
        # Actually this is useful. You could search a prefix and it should turn out false.
        if current_node.isEndOfWord == True:
            return True
        else:
            return False
    
    def startsWith(self, word : str):
        current_node = self.root

        for chr in word:
            if chr not in current_node.children:
                return False
            current_node = current_node.children[chr]
        return True



def test(functions: List[Callable], words : List[str]) -> None:
    # Don't need the object if you store funciton references
    # object = getattr(Trie, '__init__')()

    for i in range(0, len(functions)):
        # Function names stored as strings
        # print(getattr(object, functions[i])(words[i]))
        # print(i, functions[i], words[i])
        # Function references stored and used without getattr
        print(functions[i](words[i]))


# This works but is not best practice. 
functions1 : List[str]= ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]

# Storing the references to the functions that you are trying to call is better
obj = Trie()
functions2 : List[Callable] = [obj.insert, obj.search, obj.search, obj.startsWith, obj.insert, obj.search]
words : List[str] = ["apple", "apple", "app", "app", "app", "app"]


test(functions2, words)







        
        







