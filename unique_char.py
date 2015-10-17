import pdb


def unique_str(string):
    for s in string:
        for uni in string[string.index(s)+1:]:
            if s == uni:
                return False

    return True








    



if __name__ == "__main__":
    print unique_str("abcdefg")    
