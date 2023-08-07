# Paired Parentheses

# Write a function, paired_parens, that takes in a string as an argument. 
# The function should return a boolean indicating whether or not the string has well-formed parentheses.
# You may assume the string contains only alphabetic characters, '(', or ')'.


def paired_parens(string):
  # create empty stack to store first parentheses
  stack = []

  # loop through string
  for char in string:
    # if char is open parentheses 
    if char == "(":
      # save it in a stack
      stack.append(char)
    # else if char is closed parentheses
    elif char == ")":
      if len(stack) == 0:
        return False
      else:
        # pop open parentheses off stack and compare
        stack.pop(-1)
  if len(stack) == 0:
    return True
  else:
    return False






# TEST CASES
print(paired_parens("(david)((abby))")) # -> True
print(paired_parens("()rose(jeff")) # -> False
print(paired_parens(")(")) # -> False
print(paired_parens("()")) # -> True
print(paired_parens("(((potato())))")) # -> True
print(paired_parens("(())(water)()")) # -> True


# input a string with parentheses
# output true (has opening and closing parentheses), or false (does not have matching pair)