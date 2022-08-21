
# answer
# the  10001  prime number is:  104743

def primeTest(prime):
    divisor = 2

    if prime == 1:
        return False

    for i in range(prime):
        if divisor >= prime:
            break
        res = prime / divisor
        check = res.is_integer()
        if check:
            return False
        divisor = divisor + 1
    return True


def find(max):
    counter = 1
    prime_counter = 0
    while prime_counter < (max + 1):
        if primeTest(counter):
            prime_counter = prime_counter + 1
            if prime_counter == max:
                print('the ', max, ' prime number is: ', counter)
        counter = counter + 1


if __name__ == '__main__':
    find(10001)
