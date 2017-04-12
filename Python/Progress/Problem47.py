import math


def get_prime_factors(num):
    i = 2
    facs = []
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            facs.append(i)
    if num > 1:
        facs.append(num)
    return facs


if __name__ == '__main__':

    

    try:
        for i in range(4, 10000000):
            factors = set(get_prime_factors(i))
            if len(factors) == 4:
                print(i, factors)
                try:

                    for j in range(i+1, i+5):
                        temp = set(get_prime_factors(j))
                        print(j, temp)
                        if len(temp) != 4:
                            raise StopIteration
                        else:
                            print(j, temp)
                            for fac in temp:
                                if fac in factors:
                                    raise StopIteration

                    print ("this satisfies the condition: ", i)
                    raise OSError

                except StopIteration:
                    print ("i did the break")


    except OSError:
        print("python is stupid")
