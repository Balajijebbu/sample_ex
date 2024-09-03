# sample.py

# Importing necessary libraries
import random

# Function to greet the user
def greet_user(name):
    print(f"Hello, {name}! Welcome to the Python sample program.")

# Function to calculate the sum of two numbers
def calculate_sum(a, b):
    return a + b

# Function to determine if a number is even or odd
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Class to represent a simple counter
class Counter:
    def __init__(self, start=0):
        self.count = start

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def get_count(self):
        return self.count

# Main function to demonstrate the functionality
def main():
    # Greet the user
    greet_user("Balaji")

    # Demonstrating basic calculations
    num1 = 10
    num2 = 20
    total = calculate_sum(num1, num2)
    print(f"The sum of {num1} and {num2} is {total}.")

    # Checking if a number is even or odd
    number = random.randint(1, 100)
    if is_even(number):
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")

    # Using the Counter class
    counter = Counter()
    counter.increment()
    counter.increment()
    print(f"The counter value after two increments is {counter.get_count()}.")
    counter.decrement()
    print(f"The counter value after one decrement is {counter.get_count()}.")

# This ensures that the main function is executed when the script is run
if __name__ == "__main__":
    main()
