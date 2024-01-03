# Array modification Challenge - Jan 2, 2024
# Write a function that takes in 3 parameters:
# - an array of values
# - a start point (zero-based)
# - a length

# The result of the function needs to be an array containing values from the array passed in argument 1, minus the amount of elements passed in argument 3 (length), starting at the position passed in argument 2 (start).

# Example:
# result = myCoolFunction([1,2,3,4,5,6,7], 2, 1)
# # result = [1,2,4,5,6,7]

def modify_array(array, start, length):
    if start < 0 or start >= len(array):
        error = (
            f"Invalid start of {start} in {array} with length of {len(array)}")
        return error
    elif length < 0 or length > len(array):
        error = (
            f"Invalid length of {length} in {array} with length of {len(array)}")
        return error
    else:
        del array[start:start+length]
        return array
    return


print(modify_array([1, 2, 3, 4, 5, 6, 7], 2, 1))
print(modify_array(["A", "B", "C", "D", "E", "F", "G"], 2, 2))
print(modify_array(["B", "A", "N", "D", "A", "N", "A"], 3, 1))
print(modify_array([1, 2, 3, 4, 5, 6, 7, 8], 9, 4))
print(modify_array([1, 2, 3, 4], 3, 8))
print(modify_array([1, 2, 3, 4, 5, 6, 7, 8, 9,
      10, 11, 12, 13, 14, 15, 16, 17, 18], 7, 8))
