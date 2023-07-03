# Compress

# Write a function, compress, that takes in a string as an argument. 
# The function should return a compressed version of the string where consecutive occurrences of 
# the same characters are compressed into the number of occurrences followed by the character. 
# Single character occurrences should not be changed.

# 'aaa' compresses to '3a'
# 'cc' compresses to '2c'
# 't' should remain as 't'

# You can assume that the input only contains alphabetic characters.

# Two pointer solution:
# i = 0 -> end (tracks the letter)
# j = 0 -> end (tracks the occurances)

def compress(s):
    s += '.'
    result = []
    i, j = 0, 0

    while j < len(s):
        if s[i] == s[j]:
            j +=1
        else: 
            letter_count = j - i
            if letter_count == 1:
                result.append(s[i])
            else:
                result.append(str(letter_count))
                result.append(s[i])
            # Catch i up to j
            i = j        
    return ''.join(result)



# ltr_count = 
# 0 1 2 3 4 5 6 7 8 9
# c c a a a t s s s .
# i
# j

# [    ]

# TEST CASES
print(compress('ccaaatsss')) # -> '2c3at3s'
print(compress('ssssbbz')) # -> '4s2bz'
print(compress('ppoppppp')) # -> '2po5p'
print(compress('nnneeeeeeeeeeeezz')) # -> '3n12e2z'
print(compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'));  # -> '127y'

