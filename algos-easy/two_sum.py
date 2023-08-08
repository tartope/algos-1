# Two Sum

# Write a function, two_sum, that takes in a list and a target sum as arguments. 
# The function should return a tuple containing a two of indices whose elements sum to the given target. 
# The indices returned must be unique.
# Be sure to return the indices, not the elements themselves.
# There is guaranteed to be one such two that sums to the target.


def two_sum(numbers, target_sum):
    # loop through list
    # for i, num1 in enumerate(numbers):
    #     # loop through list again to compare each element to each other
    #     for j, num2 in enumerate(numbers):
    #         # if the indices are not the same
    #         if i != j:
    #             # if the sum of the elements equal the target
    #             if num1 + num2 == target_sum:
    #                 # return a tuple of the indices
    #                 return (i,j)

    # create empty dict
    map = {}
    # # loop through list
    for idx, num in enumerate(numbers):
        # create variable with complement number (target_sum - num)
        compNum = target_sum - num
        # store complement number in dict with number value
        if compNum in map:
            return (map[compNum], idx)
        else:
            map[num] = idx
        
    

# TEST CASES
print(two_sum([3, 2, 5, 4, 1], 8)) # -> (0, 2)
print(two_sum([4, 7, 9, 2, 5, 1], 5)) # -> (0, 5)
print(two_sum([4, 7, 9, 2, 5, 1], 3)) # -> (3, 5)
print(two_sum([1, 6, 7, 2], 13)) # -> (1, 2)
print(two_sum([9, 9], 18)) # -> (0, 1)
print(two_sum([6, 4, 2, 8 ], 12)) # -> (1, 3)
