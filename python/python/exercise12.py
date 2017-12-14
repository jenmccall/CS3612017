def main():
    print("Fibonacci 8: ", fibonacci(8));
    print("Fibonacci 12: ", fibonacci(12));
    
def fibonacci(x):

    if x <= 1:
        return x;

    else:
        return fibonacci(x-1) + fibonacci(x-2);
    


if __name__ == "__main__":
    main()
