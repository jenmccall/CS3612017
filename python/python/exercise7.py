def main():
    a = [0, 1, 2, 3]
    elements(a)
    reverse(a)
    print(length(a))
    

def elements(a):    
    for i in a:
        print i

def reverse(a):
    for i in reversed(a):
        print i

def length(a):
    x = 0

    for i in a:
        x += 1

    return x

if __name__ == "__main__":
    main()
