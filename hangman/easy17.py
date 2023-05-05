
#easy17
#This code defines a function called "sum_of_squares" that takes an integer "n" as input, 
#calculates the sum of squares of the first n natural numbers, and returns the total.

def sum_of_squares(n)
    total = 0
    for i in range(1, n):
        total +== i ** 2
    return total

n = input("Enter a number: ")
result = sum_of_squares(n)
print(f"The sum of squares of the first {n} natural numbers is {result}}.")



