'''

'''

from typing import Optional, List
import math


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


def createLinkedList(array):
    if len(array) == 0:
        return None
    
    head = ListNode(array[0])
    curr = head

    for i in range(1, len(array)):
        new_node = ListNode(array[i])
        curr.next = new_node
        curr = new_node
    
    return head

# head = createLinkedList([2,1])

def displayLinkedList(head):
    if head is None:
        return None
    
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next
    
# displayLinkedList(head)

# Hare and Tortoise. Delta = 3. Return middle element
def RemoveMiddleNode(head : ListNode) -> ListNode:
    if head is None:
        return None
    if head.next is None:
        return None

    if head.next.next is None:
        head.next = None
        return head
    if head.next.next.next is None:
        head.next = head.next.next
        return head

    tortoise = head
    hare = head
    behind_tortoise = None

    while hare and hare.next:
        print(f"tortoise {tortoise.val}, hare {hare.val}")

        if hare.next is None:
            # print(f"here {tortoise.val}{hare.val} {behind_tortoise.val}")
            tortoise.next = tortoise.next.next
            break
        tortoise = tortoise.next

        if hare.next.next:
            hare = hare.next.next.next
    
    return head


# Hashmap approach. O(n) space
def RemoveMiddleNode2(head: ListNode) -> ListNode:
    if head.next is None:
        return None
    myNodes = {}

    curent_node = head
    index = 0
    while curent_node:
        myNodes[index] = curent_node
        curent_node = curent_node.next
        index += 1
    
    delete_index = math.floor((index) / 2)
    # print(f"delete_index {delete_index}, index {index}")
    myNodes.get(delete_index - 1).next = myNodes.get(delete_index + 1)
    myNodes.get(delete_index).next = None

    return head


def test(lists: List[List[int]])-> None:

    for ls in lists:
        head = createLinkedList(ls)
        print("List before removal")
        displayLinkedList(head)
        modded_head = RemoveMiddleNode2(head)
        print("List after removal")
        displayLinkedList(modded_head)


tests =[[1,3,4,7,1,2,6], [1,2,3,4], [2,1], [1], [5,2,4,1,2]]
    

test(tests)



    

