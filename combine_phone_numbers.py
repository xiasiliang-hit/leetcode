
class Solution(object):
    def letterCombinations(self, digits):

        m = {u'2':'ab', u'3':'de', u'4':'gh', u'5':'jkl',u'6':'mno', u'7':'pqrs', u'8':'tuv', u'9':'wxyz'}
        
        l = []
        for i in range(0, len(digits)):
            characters = m[digits[i]]
            l.append(characters)



        combined = []
        for i in range(0, len(l)):
            ele = l[i]
            combined = self.combine_set(combined, ele)
            
        return combined

    def combine(self, xstr, ystr):
        re = []
        for ch1 in xstr:
            for ch2 in ystr:
                re.append(ch1+ch2) 
        return re
    
    def combine_set(self, xlist, ystr):
        l = []
        if len(xlist) == 0:
            l = [ ele for ele in ystr]
        
 
        for astr in xlist:
            for ch in ystr:
                l.append(astr + ch)

        
        return l


class SolutionMapReduce(object):
    def digit_map(self, digit):
        m = {u'2':'ab', u'3':'de', u'4':'gh', u'5':'jkl',u'6':'mno', u'7':'pqrs', u'8':'tuv', u'9':'wxyz'}
        return m[digit]

    def multi_map(self, arraya, arrayb):
        for a in arraya:
            for b in arrayb:
                yield a + b
                
#                l.append(a+b)
#        return l


    def begin2(self, digits):
        l = map(self.digitmap, digits)
        r = reduce(self.multi_map, l)
        for ele in r:
            print r



#    def combine_reduce(self, array, bstr):
#        for astr in array:
#             yield  map(self.multi_map, astr, bstr)

    def begin(self, digits):
        l = map(self.digit_map, digits)
        l[0] = [l[0]]
        for c in reduce(self.combine_reduce, l):
            print c


        
            
if __name__ == '__main__':
    s = Solution()
    s2 = SolutionMapReduce()
    s2.begin2("234")
#    print    s.letterCombinations('234')
