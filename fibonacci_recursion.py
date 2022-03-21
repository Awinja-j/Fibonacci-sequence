def fibonacci_recursion(n):
    # Program to display the Fibonacci sequence up to n-th term
    if n <= 1:
        return n
    else:
        return(fibonacci_recursion(n-1) + fibonacci_recursion(n-2))

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    print(fibonacci_recursion(n))