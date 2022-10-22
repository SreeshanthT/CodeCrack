"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. 
The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pass
    
if __name__ == "__main__":
    linked_list = ListNode(val=1)
    linked_list.next = ListNode(val=2)
    linked_list.next.next = ListNode(val=3)
    
    print(linked_list.val)
    print(linked_list.next.val)
    print(linked_list.next.next.val)