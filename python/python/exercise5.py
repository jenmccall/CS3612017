def main():
    number = 0
    x = 11
    
    while (number < 20):
        if (x % 5) == 0 or (x % 7) ==0 or (x % 11) == 0:
            print x
            number += 1
        x += 1

  
if __name__ == "__main__":
    main()
