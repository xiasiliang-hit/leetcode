# not running

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        result = None
        pre = None
        current1 = l1
        current2 = l2
        #for i in range(0, len(l1)):
        while current1 != None:
            newNode = ListNode(current1.val + current2.val)
            
            if pre == None:
                pre = newNode
                result = pre
            else:
                pre.next = newNode
                pre = newNode


        current = result  
        while current != None:
            if current.val >= 10:
                current.val = current.val - 10
                if current.next != None:
                    current.next.val = current.next.val + 1

            current = current.next
            
        return result
        

if __name__ == '__main__':
    l1= [2,4,3]
    l2 = [5,6,4]
    s= Solution()
    s.addTwoNumbers(l1, l2)
    
