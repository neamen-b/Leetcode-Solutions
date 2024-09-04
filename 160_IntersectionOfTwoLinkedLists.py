'''
Initial Thoughts

1. Advance from node to node.next simultaneously (for both linked lists) and see if the node.next match
    Not the value of the node, but the object itself

Problems?
a. List might not have the same length. 
    a -> b -> c -> d -> j
        e -> f -> d -> k

    they both go to d, but when on c.next (d), it will be d.next (k)

    . Ahh could keep track of which nodes have been visited in a set. Both lists add to them same set 
        for each
        List A: if node.next not in set: set.add(node.next) else: return node.next
        List B: if node.next not in set: set.add(node.next) else: return node.next
    
    Both lists keep adding to set, if it already exists, then one of them has added (seen) it before, therefore an intersection
    Has to be the first one seen because it will be similar after that. 

    Code it up and see if it works


b. ***Issue while coding
    1. The heads need to be considered an intersection if they are same as well
        So just checked if they are equal before proceeding with traversal

    2. The heads need to be added to the set.
        If one head is seen further along the chain of the other list, it should be recognized. 

    3. The lists could not be the same length. If one ends before the other, then the while loop stops and might not find
        an intersection. Rookie move

        Sol : separate while loops for both lists (kind of garbage in terms of scalability)
                Actually.... just use 'or' instead of 'and' in the while loop operator
                NOPE! Then one would go "out of bounds"

Post coding:
    1. Added both heads to set first so that they are not missed as the interseciton
    2. As long as not None, check if either node.next is in the set. if so return that node
        else: add to set and advance
'''

class ListNode:

    def __init__(self, x) -> None:
        self.val = x
        self.next = None

from typing import Optional 
class Solution:

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        # If thery are empty
        if headA is None or headB is None:
            return None
        
        # If they are equal, intersection right there
        if headA == headB:
            return headA
        
        # Nodes used for traversal/ updated after each move
        root_1 = headA
        root_2 = headB

        # To keep track of seen nodes
        myset = set()

        # Add heads in case one is seen in the other's chain
        myset = {root_1, root_2}

        # while they are not None
        while root_1 or root_2:
            
            # If not None
            if root_1:

                # Add if not in there, else return becasue interseciton
                if root_1.next not in myset: myset.add(root_1.next)
                else: return root_1.next

                # Update traversal nodes to next
                root_1 = root_1.next

            if root_2:
                # Add if not in there, else return becasue interseciton
                if root_2.next not in myset: myset.add(root_2.next)
                else: return root_2.next

                # Update traversal nodes to next
                root_2 = root_2.next

        # if none of those happened, then return none
        return None
# Testing 

sol = Solution()

A = ListNode(x=1, next=None)
B = ListNode()

