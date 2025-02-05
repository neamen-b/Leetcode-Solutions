#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution 2
class Solution:
    def deleteDuplicates(self, head):
        myset = set()
        current_node = head
        previous_node = head
        nodes = []

        if(current_node == None or current_node.next == None):
            return current_node

        while(current_node != None):

            if current_node.val in myset:
                previous_node.next = current_node.next
                # Delete node?

            else:
                myset.add(current_node.val)
                previous_node = current_node

            current_node = current_node.next
        return head


Solution.deleteDuplicates()



''' Analsyes 
    1. adding to set and list is O(1)
    2. Setup looks up is O(1)
    3. Order is dependent on while loop
        It iterates through the whole linked list
        Therefore, o(n)
'''







#Solution 1
# I did not understand what I was being passed exactly
# This is the solution when I thought that I was being passed a list of nodes
# Also, I did not understand that I had to return the head of the linked list as oppposed to the whole list

        # myset = set()
        # previous_node = head

        # for node in head:
            
        #     if node.val in myset:
        #         previous_node.next = node.next
        #         # Delete node?
        #         print("node" ,node.val)

        #     else:
        #         myset.add(node.val)
        #         previous_node = node

        # return list(myset)