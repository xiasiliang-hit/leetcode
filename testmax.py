from max_XOR import makelength
from hamming import Hamming


if __name__ == "__main__":
    (a,b) = makelength("11", "1111")
    print (a,b)
    h = Hamming()
    print h.get_hamming(1,2)

    
