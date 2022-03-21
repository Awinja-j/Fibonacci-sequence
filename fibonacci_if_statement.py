def fibonacci_if_statement(n):
    # Program to display the Fibonacci sequence up to n-th term

    nterms = n

    # first two terms
    n1, n2 = 0, 1
    count = 0

    # check if the number of terms is valid
    if nterms <= 0:
        return "Please enter a positive integer"
    
    # if there is only one term, return n1
    elif nterms == 1:
        return "Fibonacci sequence upto",nterms,":" + str(n1)

    # generate fibonacci sequence
    else:
        print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    print(fibonacci_if_statement(n))