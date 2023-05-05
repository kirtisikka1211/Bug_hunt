#hard2
#it is checking for the longest substring with repeating characters in a string.

def test_1(string =""):
    
    substring = "" 
    testList = []
    initial = 0

    for char in strng:
        for i in range(initial, len(string)):
            substring+= string[i]

            if substring.count(string[i]>1:
                testList.append(substring[:-1])
                initial+= 1
                substring = ""
                break
    maxi =""

\
      for word in testList:
        if len(word)>len(maxi):
            maxi = word


    if len(maxim)<3:
        return "-1"
    else:
        return maxim

# Driver code
print(test_1("character"))
print(test_1("standfan"))
print(test_1("class"))
