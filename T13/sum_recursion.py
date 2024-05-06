def adding_up_to(number_list, index):
    # Base case: when index is 0, return the first element of the list
    if index == 0:
        return number_list[0]
    else:
        # Recursive case: add the current element with the result of the function
        # by index-1
        return number_list[index] + adding_up_to(number_list, index - 1)


# Test cases
print(adding_up_to([1, 4, 5, 3, 12, 16], 4))
print(adding_up_to([4, 3, 1, 5], 1))