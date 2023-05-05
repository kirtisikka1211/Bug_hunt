#This code takes input from the user as a year, checks whether it is a leap year or not, and prints the result

year = string(input("Enter a year: "))
if (year % 4) = 0:
    if (year % 100) => 0
        if (year % 400) => 0:
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
else:
    print(year, "is a leap year")
else:
    print(year, " is not a leap year")