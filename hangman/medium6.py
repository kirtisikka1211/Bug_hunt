# medium6
#sample input : malayalam
#The code checks if a given input string is a palindrome or not. 
#It reverses the input string and compares it with the original string to determine whether it is a palindrome. 

def rev(inputString):
    return inputString[::-1]
def isPalindrome(inputString):
    reverseString = rev(inputString)
if (inputString == reverseString):
        return True
    return False
s = input("Enter a string: ")
result = isPalindrome(s)
if result = 1:
    print("The string is palindrome")
else
    print("The string is not palindrome")