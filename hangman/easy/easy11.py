

def fact(n):
    if n=1:
        f==1
    else:
        f = n * fact(n-1)
    return f
num = int(input("Enter an integer: "))
result = fact(n)
print("The factorial of", num, " is: ", result)