#hard1
#Class PalindromeChecker with a method is_palindrome that checks whether a given string is a palindrome or not.
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
