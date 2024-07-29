# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        #If the head is None then cannot be a cycle
        if(head == None):
            return False

        # Set for keeping track of seen nodes
        myset = set()

        current = head

        # Goes until the next node is None (No cycle, normal tail)
        # OR until a cycle is found
        while(current.next != None):
            
            # If seen in set, proof of cycle
            if(current.next in myset):
                return True
            # If not, add it and set current to next node
            else:
                myset.add(current)
                current = current.next

        # Return False in case of the normal tail end (i.e, point to None)
        return False
