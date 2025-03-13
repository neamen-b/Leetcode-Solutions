'''

initial thoughds

seperately create the odd and even list, then join end of odd to beginning of even
'''


from typing import Optional, List


class ListNode:

    def __init__ (self, val : int = 0, next = None) -> None:
        self.val = val
        self.next = next



def oddEvenList (head : Optional[ListNode]) -> Optional[ListNode]:
    # empty linked list
    if head is None:
        return None
    # One node in linked list
    if head.next is None:
        return head

    odd_head = head
    even_head = head.next


    curr_odd = odd_head
    curr_even = even_head
    """ Even number of nodes? ending is even ELSE ending is odd
        if even """

    while (curr_even and curr_even.next):
        print("before", curr_odd.val, curr_even.val)
        curr_odd.next = curr_even.next
        curr_odd = curr_odd.next
        curr_even.next = curr_odd.next
        curr_even = curr_even.next

        # if curr_even.next is None:
        #     break
        # print("after", curr_odd.val, curr_even.val)

    
    curr_odd.next = even_head
    return odd_head

odd_length_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
even_length_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

test_cases : List[ListNode] = [odd_length_list, even_length_list]
def test(test_cases):

    for head in test_cases:
        new_head = oddEvenList(head)
        curr = new_head
        while curr:
            print(curr.val)
            curr = curr.next

test(test_cases)


