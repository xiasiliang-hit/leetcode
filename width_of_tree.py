class Node(object):
    data = 0
    child = []

class Tree():
    root = None
#    build_tree() 

def width(tree):
    queue = []
    queue_next = []

    queue.append(root)

    i = 0
    max_i = 1
    
    while len(quueu) != 0:
      i = i + 1
      while len(queue) != 0:
        queue_next = queue_next + queue.pop()

      if len(queue_next) > max_i:
        max_i = len(queue_next)

      queue = queue_next
    return max_i
    
if __name__ == "__main__":
    t = Tree
    
    a = [1,2,3]
    b=  [5,4]
    c = [6,7]

    f = lambda x :  i in x

    arr = [a,b,c]

    def ad(x, y): x + y 

    print [a + b]
    
    arr3 = reduce(ad, arr)

    arr2 = (f, arr)
    print arr3
