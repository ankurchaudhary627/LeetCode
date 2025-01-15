# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr=l1
        n1=0
        i=1
        while curr:
            n1=(curr.val*i)+n1
            i*=10
            curr=curr.next
        i=1
        curr=l2
        n2=0
        while curr:
            n2=(curr.val*i)+n2
            i*=10
            curr=curr.next
        res=n1+n2
        print(n1,n2,res)
        dummy=ListNode(0)
        prev=dummy
        while True:
            temp = res%10
            res=res//10
            node = ListNode(temp)
            prev.next=node
            prev=node
            if res==0:
                break
        return dummy.next