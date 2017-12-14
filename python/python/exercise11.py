def main():
    n = [1, 4, 9, 16]
    print(iteration(n))
    print(recursion(n))

def iteration(n):
    product = 1
    for i in n:
        product *= i
    return product

def recursion(n):    
    length = len(n)
    newlist = n
    product = 1

    if len(newlist) == 0:
        return product
    else:
        product = newlist.pop(0)
        return product * recursion(newlist)

if __name__ == "__main__":
    main()
