#! not working, list created is not linked
#! can use origanl llist

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import pdb

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if (l1 == None):
            return l2
        elif (l2 == None):
            return l1


        tail1,c1 = self.reverseLinkedList(l1)
        tail2,c2 = self.reverseLinkedList(l2)

        
        l = None
        head = None
        while (l1 != None or l2 != None ):
            a = l1.val + l2.val
            n = ListNode(a)
#            n.val = a
            if l == None:
                l = n
                head = copy.deepcopy(n)
            else:
                l.next = n
                l = l.next

            l1 = l1.next
            l2 = l2.next
            
            
#        if l1.nexta == None:
        while (l2 != None ):
                n = ListNode(l2.val)
                
                
                # if l == None:
                #     l = n
                # else:
                l.next = n

                l1 = l1.next
                l = l.next
            
 #       else:
        while (l1 != None):
                n = ListNode(l1.val)

                # if l == None:
                #     l = n
                # else:
                l.next = n

                l1 = l1.next
                l = l.next

        c = head
        bit = 0
        while (c != None):
            if c.val+bit >= 10:
                c.val = 0
                bit = 1  
                c = c.next
            else:
                c = c.next
            
        a = self.reverseLinkedList(head)
                
#        self.pprint(head)
#        self.pprint(a)
        return self.pprint(a)
    
        
    def reverseLinkedList(self, li):
        count = 0
        current = li
        previous = None
        while (current != None):
            npointer = current.next
            current.next = previous

            previous = current
            current = npointer


        return previous, count
        
    def pprint(self, li):
        array = []
        while li != None:
            print li.val,
            array.append(li.val)
            li = li.next
        
        return array
        
        
if __name__ == "__main__":
    a = [1,2,3]
    b = copy.copy(a)
    a = [1,2,3,4,5]
    
    
    print b
    

