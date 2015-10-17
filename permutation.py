import pdb
import sys

def booking_test2(self):
    i = (int)(sys.stdin.readline())

    data = []
    lines_raw = sys.stdin.readlines()

    lines = [x.replace(' ', '') for x in lines_raw]
    lines2 = [l for l in lines2]

    result = []

    for l in lines:
        per = permutation(l)
        
        one_re = []
        for l2 in list(lines2):
            if l2 in per:
                one_re.append(one_re)
                lines2.remove(l2)

        r = ""
        for word in sorted(one_re):
            r = r + word + ","
            result.append(r)
        
    for line in sorted(result):
        print line
        

#return list
def permutations(string, step = 0):

#    if string == "":
#        return [""]
    
    # if we've gotten to the end, print the permutation
    if step == len(string):
        print "".join(string)
        #l.apppend("".join(string))
        
    # everything to the right of step has not been swapped yet
    for i in range(step, len(string)):

        # copy the string (store as array)
        string_copy = [character for character in string]

        # swap the current index with the step
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]

        # recurse on the portion of the string that has not been swapped yet (now it's index will begin with step + 1)
        permutations(string_copy, step + 1)




def permutations2(mystr):
    if len(mystr) <= 1:
        return [mystr]
    res = []
    for elt in mystr:
        permutations = permutations2(mystr.replace(elt, ""))
        for permutation in permutations:
            res.append(elt + permutation)
    return res

        
if __name__ == '__main__':
    l = permutations2('a')
    print l
