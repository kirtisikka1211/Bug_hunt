#This code defines a function called "count_vowels" that takes a string as input, counts the number of vowels in the input string, and returns the count.
# The code then calls this function for three different input strings and prints the results. 

def count_vowels(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for word in sentence.split():
        for letter in word:
            if letter in vowels:
                count += 1
    return count

print(count_vowels("The quick brown fox jumps over the lazy dog"))
print(count_vowels("Hello, World!"))
print(count_vowels("Python is a high-level programming language."))

print(count) # NameError: name 'count' is not defined
