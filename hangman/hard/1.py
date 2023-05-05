



class PalindromeChecker:
  def __init__(self, string)
    self.string = string

  def is_palindrome(self)
  start, end = 0, len(self.string) - 1
    while start < end
      if self.string[start] != self.string[end]:
          return False
        start += 1
        end -= 1
      return True




#ans


# class PalindromeChecker:
#     def __init__(self, string):
#         self.string = string
    
#     def is_palindrome(self):
#         start, end = 0, len(self.string) - 1
#         while start < end:
#             if self.string[start] != self.string[end]:
#                 return False
#             start += 1
#             end -= 1
#         return True
