import pdb
import Queue


# input [(1,2) (2,3) (1,3)]
def friend_circle(li, given_num):
    di = {}
    for pair in li:
        if pair[0] in di.keys():
            di[pair[0]].append(pair[1])
        else:
            di[pair[0]] = [pair[1]]

    q = Queue.Queue()
    q.put(given_num)

    re = []
    while (q.qsize() != 0):

         ele = q.get()
         for fri in di[ele]:
                q.put(fri)

                if fri not in re:
                    re.append[fri]
                else:
                    continue
    return re




if __name__ == '__main__':
    inp = [(1,2), (2,3), (1,3)] 
    friend_circle(inp, 1)
