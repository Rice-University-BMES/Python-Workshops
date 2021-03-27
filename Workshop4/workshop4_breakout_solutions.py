# Rice BMES Python Workshop 4 Breakout Room Solutions

# author Eric Torres
# email edt3@rice.edu
# date 27 Mar 2021


# Object-Oriented Programming

# You have just been hired to make the bank account system at a new bank! You will implement the account system using a
# class called BankAccount.

# Make this class with an attribute of "balance", and make it such that when you initialize an account you can input the amount
# of money it starts out with

class BankAccount:

    def __init__(self, initial_amount):
        self.balance = initial_amount


# Now that you made your initialization method, add a method that will return your current balance! Call it "get_balance"
    def get_balance(self):
        print("Balance = " + str(self.balance))


# Create methods to deposit and withdraw money from your account!

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if (amount <= self.balance):
            self.balance -= amount
        else:
            self.balance = 0

# You just remembered you can't let people withdraw more money than what's in their account! Make appropriate changes
# to your withdraw method so that people can withdraw all of their money but not end up with a negative balance

# (solution implemented above)

# Now that you have your system in place, try it out yourself! Test our your methods and see what happens


##############################################################################################################

# Recursion

# For this example, you will be writing a function "find_factorial" that calculates the factorial of a number (ex: 5! = 120)
# First define your base and recursive cases, then write the function such that the recursive case calls the function but
# with less data

def find_factorial(n):
    if n == 1:
        return 1
    else:
        return n * find_factorial(n-1)

print(find_factorial(5))