# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def get_list(self):
        if self.next is not None:
            n = self.next
            l_list = []
            while n is not None:
                l_list.append(n.val)
                n = n.next
            return l_list
        else:
            return [self.val]
class Solution:
    def addTwoNumbers(self, l1:ListNode, l2:ListNode) -> ListNode:
        carry,sum_node = 0,ListNode()
        sum_node_temp = sum_node
        
        while l1 is not None or l2 is not None or carry != 0:
            
            node_val1 = l1.val if l1 is not None else 0
            node_val2 = l2.val if l2 is not None else 0
            
            sum_with_carry = node_val1 + node_val2 + carry
            carry = sum_with_carry//10
            sum_without_carry = sum_with_carry % 10
            sum_node_temp.next = ListNode(val=sum_without_carry)
            sum_node_temp = sum_node_temp.next
            
            print(sum_node_temp.val)
            # print(f"{l1.val} + {l2.val} = {sum_with_carry} carry:{sum_with_carry//10}, sum:{sum_without_carry}")
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
                

        print(sum_node.get_list())
        return sum_node.next
        
l1=ListNode(val=2,next=ListNode(
    val=4,next=ListNode(
            val=3,next=None
        )
    )
)
l2=ListNode(val=5,next=ListNode(
    val=6,next=None
    )
)
x = Solution()
x.addTwoNumbers(l1,l2)