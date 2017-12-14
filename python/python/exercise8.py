def main():
    a = [12, 14, 16]
    b = a
    c = a[:]

    print a
    print b
    print c

    c[2] = 10

    print a
    print b
    print c

    l = [1, 1, 1, 2, 3, 5]
    print(set_first_elem_to_zero(l))
    

def set_first_elem_to_zero(l):
    new = l[:]

    new[0] = 0

    return new   

if __name__ == "__main__":
    main()
