from threading import Thread

# A thread class to produce Fibonacci Numbers

class FibonacciThread(Thread):
    def __init__(self, n):
        Thread.__init__(self)
        self.n = n
    def run(self):
        print("Fibonacci Thread Started")

        firstTerm   = 0

        secondTerm  = 1

        nextTerm    = 0

        if self.n <= 1:
            return ("Fibonacci sequence upto {} is {}".format(self.n, str(firstTerm)))    


        for i in range(0, self.n):

            if ( i <= 1 ):

                nextTerm = i

            else:

                nextTerm    = firstTerm + secondTerm

                firstTerm   = secondTerm

                secondTerm  = nextTerm

 

            print(nextTerm)

 

        print("Fibonacci Thread Ending")      

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    fibonacciThread = FibonacciThread(n)
    fibonacciThread.start()  
    