import pdb

class Hamming(object):
    def get_hamming (self, a, b):
        abin = "{0:b}".format(a, 2)
        bbin = "{0:b}".format(b, 2)

        if (len(abin) > len(bbin)):
            dis = len(abin) - len(bbin)
            bbin = '0'*dis + bbin
        else:
            dis = len(bbin) - len(abin)
            abin = '0'*dis + abin

#        print abin
#        print bbin

        hamming = 0
        for i in range(0, max(len(abin), len(bbin)) ):
            if abin[i] != bbin[i]:
                hamming = hamming + 1
        return hamming


    def get_total_hamming(self, array):
        re = []
        total_hamming = 0
        for e1 in array:
            for i in range(array.index(e1), len(array)):
                e2 = array[i]
                re.append([e1, e2])
        for couple in re:
            a = couple[0]
            b = couple[1]

#            print self.gethamming(a,b)
            total_hamming = total_hamming + self.get_hamming(a,b)

        return total_hamming

    
if __name__ == '__main__':
    h = Hamming()
    print h.gethamming(1,8)
    
    a = [1,2,3]
    print h.get_total_hamming(a)
    

