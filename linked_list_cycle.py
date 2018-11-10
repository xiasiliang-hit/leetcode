# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if head == None or head.next == None :
            return False
        
        slow = head
        fast = head.next
        while fast != None and fast.next != None:
            if fast == slow:
                return True
            else:
                fast = fast.next.next
                slow = slow.next
                
        return False


# wrong becasue record all the node line 70

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
address=[]
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if hasCycle(head):
            print address
            current = head
            while current != None:
                if current in address:
                    return current
                else:
                    pass
                current = current.next
                
        else:
            return None
                   
def hasCycle(head):
        if head == None or head.next == None :
            return False
        
        slow = head
        fast = head.next
        while fast != None and fast.next != None:
            address.append(slow)
            
            if fast == slow:
                return True
            else:
                fast = fast.next.next
                slow = slow.next
                
        return False
        
        
