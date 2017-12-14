def main():
    a = [[1,3], [3,6], [8,10,12]]

    print(a)
    print(sublist(a))

def sublist(a):
    s = []

    length = len(a)

    for i in range(0, length):
        templist = a[i] #when the item is a list, we separate it and make it it's own list.
        templength = len(a[i]) #this is the length of that new list

        for x in range(0, templength):
            s.append(templist[x]) #puts the items in the sublist into this new list of elements.
            x = x + 1     

    return s

if __name__ == "__main__":
    main()
