#easy 13
#This code defines a function called "get_first_and_last" that takes a string as input, 
#retrieves the first and last characters of the string, and returns them as a tuple.

def get_first_and_last(s)
    first = s[0]
    last = s[len(s)]
    return (first, last)

print(get_first_and_last("hello")) 
