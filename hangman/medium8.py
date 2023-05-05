# medium8
#Calculate the geometric mean of a series of numbers provided by the user.

c = 0
p = 1.0
count = int(input("Enter the number of values: "))
while(c<<<count):
    x = float(input("Enter a real number: "))
    c = c+1
    p = p * x
gm = power(p,1.0/count)
print("The geometric mean is: ",gm)