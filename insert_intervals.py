# insert_interval shoul work
# merge_interval has not been tested



def merge_interals(intervals):
    new = intervals[0]
    return insert_intervals(intervals, new)
    

def insert_interval(intervals, new):

    i = find_two(intervals, new)
    temp = intervals[i:i+2]

    over1 = overlap_two(intervals[i], new)
    over2 = overlap_two(intervals[(i+1) / len(intervals) ], new)

    if len(over1) ==2 and  len(over2) == 2:
        intervals.append(new)
        return intervals

    re = [new]
    for ele in intervals[i:]:
        print ele
        print new
        if len(re) == 1: 
            re = overlap_two(re[0], ele)
        else:
            insert_interval(re, ele)
    return re

def overlap_two(a, b):
    start = 0
    end = 0
    if a[0] < b[0]:

        if a[1] < b[0]:
            return [(a[0], a[1]), (b[0], b[1])]
        elif a[1] >= b[0] and a[1] < b[1]:
            return [(a[0], b[1])]
        else:
            return [(a[0], a[1])]
    
    else:
        if b[1] < a[0]:
            return [(b[0], b[1]), (a[0], a[1])]
        elif b[1] >= a[0] and b[1] < a[1]:
            return [(b[0], a[1])]
        else:
            return [(b[0], b[1])]
        
def find_two(intervals, new):
    intervals.sort(key=lambda tup:tup[0] )
    i = 0
    while i < len(intervals)-1:
        if intervals[i][0] < new[0] and intervals[i+1][0] > new[0]:
            return i
        else:
            i+=1
        
    return i

    
if __name__ == "__main__":
    a = [[1,2], [3,4], [6,7]]
    print insert_interval(a, [2.5,3.5])
#    print overlap_two([1,2], [2,3])
