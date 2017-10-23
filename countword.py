import pdb

class Solution(object):
    def __init__ (self):
        return 

    def countword(self):
        f = file("/Users/danny/Downloads/bible.txt", "r")
        d = {}
        lines = f.readlines()
        for line in lines:
            word = line.split(' ')
            if word in d.keys():
                d[word] = d[word] + 1
            else:
                d[word] = 1
        return d
    
if __name__ == "__main__":
     s = Solution()
     d = s.countword()
     print d
