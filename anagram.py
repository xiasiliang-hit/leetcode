import permutation as p





def anagram(s, t):
    if s in p.permutations2(t):
        return True

    else:
        return False



if __name__ == '__main__':
    print anagram("abcdefg", "gfedcba")

