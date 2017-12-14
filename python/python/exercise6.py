def main():
    n = 10
    print(is_prime(n))
    print(six_prime(n))
    print(up_to_prime(n))
    print(first_prime(n))

def is_prime(n):
    prime = False

    if (n%2 == 0 & n != 2):
        prime = False
    elif (n%3 == 0 & n != 3):
        prime = False
    elif (n%5 == 0 & n != 5):
        prime = False
    elif (n%7 == 0 & n != 7):
        prime == False
    elif (n%11 == 0 & n != 11):
        prime == False
    elif (n%13 == 0 & n != 13):
        prime = False
    else:
        prime = True
    
    
    if n < 2:
        prime = False
    elif n == 2 or n == 3 or n == 5 or n == 7 or n == 11 or n == 13:
        prime = True

    return prime

def six_prime(n):
    prime = False
    
    if (n+1)%6 == 0:
        if n%2 == 0:
            prime = False
        else:
            prime = True
    if (n-1)%6 == 0:
        if n%2 == 0:
            prime = False
        else:
            prime = True
    
    if n < 2:
        prime = False
    elif n == 2 or n == 3:
        prime = True

    return prime

#I'll put my items in a list because a loop with return in it
#wouldn't work for multiple values. Print would return these,
#but I don't want print in any other method than main

def up_to_prime(n):
    primes = []
    
    f = 0

    while (f <= n):
        if (is_prime(f) == True):
            primes.append(f)
            f = f + 1
        else:
            f = f + 1

    return primes


def first_prime(n):
    primes = []
    
    y = 0
    count = 1
    
    while (count <= n):
        if (is_prime(y) == True):
            primes.append(y)
            y = y + 1
            count = count + 1
        else:
            y = y + 1

    return primes

  
if __name__ == "__main__":
    main()
