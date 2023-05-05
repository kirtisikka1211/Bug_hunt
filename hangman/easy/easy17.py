# Program to find the sum of squares of the first n natural numbers

def sum_of_squares(n)
    total = 0
    for i in range(1, n):
        total +== i ** 2
    return total

n = input("Enter a number: ")
result = sum_of_squares(n)
print(f"The sum of squares of the first {n} natural numbers is {result}}.")



