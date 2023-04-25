# The code uses threading in Python to compute the factorial and sum of digits of a given number simultaneously

import threading

# A class to compute the factorial of a given number
class FactorialThread(threading.Thread):
    def __init__(self, number):
        threading.Thread.__init__(self)
        self.number = number

    def run(self):
        fact = 1
        for i in range(1, self.number + 1):
            fact = fact * i
        print("Factorial of {} is {}".format(self.number, fact))

# A class to compute the sum of digits of a given number
class SumOfDigitsThread(threading.Thread):
    def __init__(self, number):
        threading.Thread.__init__(self)
        self.number = number

    def run(self):
        sum_of_digits = 0
        for digit in str(self.number):
            sum_of_digits += int(digit)
        print("Sum of digits of {} is {}".format(self.number, sum_of_digits))


number = 12
factorial_thread = FactorialThread(number)
sum_of_digits_thread = SumOfDigitsThread(number)

# Start both threads
factorial_thread.start()
sum_of_digits_thread.start()

# Wait for both threads to complete
factorial_thread.join()
sum_of_digits_thread.join()
