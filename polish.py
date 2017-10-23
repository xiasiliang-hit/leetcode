import pdb

class Solution(object):
    def __init__(self):
        return

    def polish(self, expression):
        stack = []
        for ele in expression:
#            print 'ele' + ele
#            print stack
            if ele in ['+', '-', '*', '/']:
                
                b = stack.pop()
                a = stack.pop()

                if (ele == '+'):
                    stack.append(a+b)
                elif (ele=='-') :
                    stack.append(a-b)
                elif (ele == '*'):
                    stack.append(a*b)
                else:
                #    print a
                #    print b
                    stack.append(a/b)

            else:
                stack.append(int(ele))
        return stack.pop()

if __name__ == '__main__':
    s = Solution()
    print s.polish(["4", "13", "5", "/", "+"])
