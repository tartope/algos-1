# Anagrams

# Write a function, anagrams, that takes in two strings as arguments. 
# The function should return a boolean indicating whether or not the strings are anagrams. 
# Anagrams are strings that contain the same characters, but in any order.

def anagrams(s1, s2):
    
  # First, check for strings lengths
  if len(s1) != len(s2): return False

  # Initialize a dict to hold the letters present in first string
  count = {}
  for char in s1:
    if char not in count:
      count[char] = 1
    else:
      count[char] +=1

  # Loop through second dictionary 
  for char in s2:
    # If char is not in dict
    if char not in count:
      # Return False
      return False
    else:
      # Else if char is in dict, decrement the value
      count[char] -= 1
      # If the value is negative, return False
      if count[char] < 0:
        return False
  # After the for loop is done, return True
  return True    





# # TEST CASES
# print(anagrams('restful', 'fluster')) # -> True
# print(anagrams('cats', 'tocs')) # -> False
# anagrams('monkeyswrite', 'newyorktimes') # -> True
# anagrams('paper', 'reapa') # -> False
# anagrams('elbow', 'below') # -> True
# anagrams('tax', 'taxi') # -> False
# anagrams('taxi', 'tax') # -> False
# anagrams('night', 'thing') # -> True
# anagrams('po', 'popp') # -> False
# anagrams('pp', 'oo') # -> False
