# Rice BMES Python Workshop 4 - Recursion

# author Eric Torres
# email edt3@rice.edu
# date 27 Mar 2021


"""

Recursion: it's a way to make complex programs more succinct

it involves writing a function that calls itself from within, but with less data (otherwise it would run forever)

it works best when the data is composed of common sub-structures


define a base case and a recursive case
- base: when you know the answer to it or can solve it directly (without calling the function again)
- recursive: when you don't know and can figure it out by breaking down the problem into a smaller step

"""

# Recursion
def sum_up_to(n):
    if n == 1:
        # Base case
        return 1
    else:
        # Recursive case
        return n + sum_up_to(n-1)
    
print(sum_up_to(3))
print(sum_up_to(15))


# Same thing as...
print(sum(range(16))) # Just showing how recursion works, not necessarily convenient


def is_palindrome(word):
    if len(word) < 2:
        # Base case
        return True
    else:
        # Recursive case
        if word[0] != word[-1]:
            return False
        else:
            return is_palindrome(word[1:-1])
        
# if word is at 0 or 1 letters, you are at the center of the word, and it is then a palindrome
print(is_palindrome("aa"))
print(is_palindrome("BIOE"))
print(is_palindrome("BIOEOIB"))


print("===")

# another example you can look at on your own!
class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def get_data(self):
        print(f'{self.real}+{self.imag}j')
