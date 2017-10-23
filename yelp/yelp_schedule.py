import pdb


def make_schedule(datemap):
    re = {}
    for ind in datemap:

#        schedule = []
        l = 0
        schedule = mak_for_a_date(datemap[ind])
        while l != len(schedule) :
            l = len(schedule)
            schedule =  mak_for_a_date(schedule)
                                  
        re[ind] = schedule

    return re

def mak_for_a_date(li):
#    for time_pair in li:

    if (len(li) == 1):
        return li
    else:

        sorted_pairs = sorted(li, key=lambda x: x[0])
        re = []


        current = sorted_pairs[0]
        for i in range(1, len(sorted_pairs)):
            item1 = current
            item2 = sorted_pairs[i]
            
            if item1[1] >= item2[0]:
                
            
                if item1[0] < item2[0]:
                    start =  item1[0]
                else:
                    start = item2[0]
                    
                if item1[1] > item2[1]:
                    end = item1[1]
                else :
                    end = item2[1]

                current = [start, end]

                print [current] + sorted_pairs[2:]
                return [current] + sorted_pairs[2:]
            else:
                return sorted_pairs


    
if __name__ == '__main__':
    di = {}
    di["mon"] = [[100, 300], [400, 600], [300, 500], [600, 900]]
    di["Thu"] = [[100, 300], [400, 600], [300, 500], [800, 900]]

    print make_schedule(di)
