def test_1(string =""):
    # initializing the substring
    substring = "" 
    testList = []
    initial = 0

    # introducing a typo in the string variable name
    for char in strng:
        for i in range(initial, len(string)):
            substring+= string[i]

            # introducing a syntax error in the if statement
            if substring.count(string[i]>1:
                testList.append(substring[:-1])
                initial+= 1
                substring = ""
                break
    maxi =""

    # introducing an indentation error
      for word in testList:
        if len(word)>len(maxi):
            maxi = word

    # introducing a NameError by misspelling a variable name
    if len(maxim)<3:
        return "-1"
    else:
        return maxim

# Driver code
print(test_1("character"))
print(test_1("standfan"))
print(test_1("class"))


# def test_1(string =""):
       
#     # initializing the substring
#     substring = "" 
#     testList = []
#     initial = 0
       
#     for char in string:
           
#         for i in range(initial, len(string)):
#             substring+= string[i]
               
#             # checking conditions
#             if substring.count(string[i])>1:
#                 testList.append(substring[:-1])
#                 initial+= 1
#                 substring = ""
#                 break
#     maxi =""
       
#     for word in testList:
           
#         if len(word)>len(maxi):
#             maxi = word
               
#     if len(maxi)<3:
#         return "-1"
#     else:
#         return maxi
       
# # Driver code
# print(test_1("character"))
# print(test_1("standfan"))
# print(test_1("class"))