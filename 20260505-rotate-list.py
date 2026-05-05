# https://leetcode.com/problems/rotate-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Store current head
        cur_head = head
        new_head = None
        counter = 1
        # Base cases 1 : Null or no rotation
        if head == None or k == 0 :
            return head
        # Count the nodes
        while head.next != None :
            head = head.next
            counter += 1
        # Base cases 2 : 1 node or rotation multiple of N
        if counter == 1 or k%counter == 0 :
            return cur_head 
        # Remove loops
        k = (k%counter)
        counter -= k
        # Move k nodes forward 
        head = cur_head
        while counter > 1 :
            head = head.next
            counter -= 1
        # Assign next as new head 
        new_head = head.next
        # Assign new next as Null (break the chain)
        head.next = None
        # Iterate until end and chain last node to old head
        head = new_head
        while head.next != None :
            head = head.next
        head.next = cur_head
        # Assign new head as the solution
        return new_head
