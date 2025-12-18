#<<<<<<< feature/binet
import math

def binet(n):
    sqrt5 = math.sqrt(5)
    phi = (1 + sqrt5) / 2
    psi = (1 - sqrt5) / 2
    return round((phi ** n - psi ** n) / sqrt5)


if __name__ == '__main__':
    print(binet(6))
#=======
#def fibo(n):
#    if n < 2:
#        return n
#    else:
#        return fibo(n-1) + fibo(n-2)
#
#if __name__ == '__main__':
#    print(fibo(6))
#>>>>>>> main
