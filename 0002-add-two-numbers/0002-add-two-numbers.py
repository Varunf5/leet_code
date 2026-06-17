# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d=ListNode(0)
        temp=d
        c=0
        
        while l1 or l2:
            sum=c
            if l1:
                sum+=l1.val
                l1=l1.next
            if l2:
                sum+=l2.val
                l2=l2.next
            c=sum//10
            digit=sum%10
            temp.next=ListNode(digit)
            temp=temp.next
        if c:
            temp.next=ListNode(c)
        return d.next
        


        