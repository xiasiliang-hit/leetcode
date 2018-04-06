# minor corner cases

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if s == "":
            return 0
        if len(s) == 1:
            if mm(int(s[0])) == "$":
                return 0
            else:
                return 1
        
        m = {}
        
        i = 2
        d = {}
        d[0] = [mm(int(s[0]))]
        
        
        d[1] = [ d[0][0] + mm(int(s[1])), mm(int(s[:2])) ]
                          
        while i < len(s):
            d[i] = []
            for ele in d[i-1]:
                #if mm(int(s[i])) == "$":
                #    return 0
                print "here1"
                d[i].append( ele + mm(int(s[i])) )

            if (s[i-1] == '0'):  # skip when begin with '0'
                continue
                
            else:
                print s[i-1 : i+1]
                inte = int(s[i-1 : i+1])
                if (inte >= 1 and inte <= 26):
                    for ele in d[i-2]:
                        print "here2"
                        print d
                        d[i].append( ele + mm(inte))

        print d[len(s) - 1]
        re = []
        for ele in d[len(s) - 1]:
            if ele.find('$') == -1:
                re.append(ele)
            
        print re
        return len( re )

def mm(inte):
    if inte < 1 or inte > 26:
        return "$" # error this int
    else:
        return str(unichr(64 + inte) )
