# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):

        num1, num2 = [],[]       
        l1_curr = l1
        l2_curr = l2

        while l1_curr:
            num1.append(str(l1_curr.val))
            l1_curr = l1_curr.next
        while l2_curr:
            num2.append(str(l2_curr.val))
            l2_curr = l2_curr.next

        num1, num2 = num1[::-1],num2[::-1]
        sum = int(''.join(num1)) + int(''.join(num2))
        str_sum = str(sum)[::-1]

        # print("sum reversed", str_sum)
        new_head = ListNode(int(str_sum[0]))
        # print("new head", new_head.val)
        new_curr = new_head

        for i in range(1, len(str_sum)):
            # print("str at i", str_sum[i])
            node = ListNode(int(str_sum[i]))
            new_curr.next = node
            new_curr = node
        # print(new_head.next)
        return new_head

 

l1 = ListNode(1)

l1.next = ListNode(3)

l2 = ListNode(2)

l2.next = ListNode(4)

# print(addTwoNumbers(l1, l2).val)


# Apparently this can be solved recursilvely
# and here ius the recursive approach 11/12/2025


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import math
from typing import Optional

def traverselist(self, node: ListNode, count : int) -> int:

        if node.next is None:
            return (10 ** count) * node.val
        
        return (10 ** count) * node.val + self.traverselist(node.next, count + 1)

def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        sum_of_numbers = self.traverselist(l1, count = 0) + self.traverselist(l2, count = 0)
        # print(f"sum of numbers = {sum_of_numbers}")

        # Build a new linked list

        quotient = sum_of_numbers
        new_head = ListNode(int(quotient % 10), None)
        curr_node = new_head
        quotient = quotient // 10

        while(quotient != 0):
            print(f"quotient {quotient}")
            remainder = quotient % 10
            new_node = ListNode(int(remainder))
            curr_node.next = new_node
            curr_node = new_node
            quotient = quotient // 10
        
        return new_head


        
        
