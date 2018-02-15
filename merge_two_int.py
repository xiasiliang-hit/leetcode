# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def __init__(self):
        self.a = []
        
        return
    
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c1 = l1
        c2 = l2
        while c1 != None and c2 != None:
            if c1.val < c2.val:
                self.add(c1.val)
                c1 = c1.next
            else:
                self.add(c2.val)
                c2 = c2.next
                
        if c1 == None:
            while c2 != None:
                self.add(c2.val)
                c2 = c2.next
        else:
            while c1 != None:
                self.add(c1.val)
                c1 = c1.next
        
        return self.a
    
    def add(self, val):
        self.a.append(val)

        return
            
            