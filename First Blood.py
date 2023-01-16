#https://www.codewars.com/kata/562c04fc8546d8147b000039

import math

def prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    max_div = math.floor(math.sqrt(n))
    for d in range(3,max_div + 1,2):
        if n % d == 0:
            return False
    return True

def prime_sum(n):
    sum = 0
    while n % 2 == 0:
        sum += 2
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):
    #ekleme 2 bitis
        while n % i == 0:
                n /= i
                sum += i
        if n > 2:
            sum +=n
        return sum

def div(n):
    if(n == 1):
        return 1
    sum = n+1
    for i in range(2,(int)(math.sqrt(n))+1) :
        if (n % i == 0) :
            if (i == (n/i)) :
                sum = sum + i
            else :
                sum = sum + (i + n//i)
    return sum


def ds_multof_pfs(nMin, nMax):
    liste = []
    for i in range(nMin,nMax+1):
        birKereHesaplasakYeterli = prime_sum(i)
        if  birKereHesaplasakYeterli != 0:
            if div(i) % birKereHesaplasakYeterli == 0:
                liste.append(i)
    return liste
