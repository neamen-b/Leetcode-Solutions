# Defition of a singly linked list
from typing import Optional
class ListNode:

    def __init__(self, x: int):
        self.val = x
        self.next = None

a = ListNode(1)
# a.next = a
b = ListNode(2)
# b.next = a
c = ListNode(3)
a.next = b
b.next = c

def detectcycle(head: Optional[ListNode])-> Optional[ListNode]:

    # Empty Linked list canno have a cycle
    if head is None:
        return None
    # if there is no node that head points to, including itself, there cannot be a cycle
    if head.next == None:
        return None
    
    # Loop control. 
    cycle_found = False

    # Two pointers. Both set to the head as a starting point
    tortoise, hare = head, head

    # While a cycle is not detected. 
    while  hare.next and hare.next.next:
        # print(hare.val)
        # Ran into no attribute issue
        # if tortoise.next is not None and hare.next is not None:
        # if hare.next.next:
        tortoise = tortoise.next
        hare = hare.next.next
        
        if tortoise == hare:
                cycle_found = True
                tortoise = head

                cycle_loc_found = False

                while not cycle_loc_found:

                    if tortoise == hare:
                        cycle_loc_found = True
                        return tortoise.val
                    
                    tortoise = tortoise.next
                    hare = hare.next
    return None

print(detectcycle(a))
