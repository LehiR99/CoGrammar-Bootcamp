def largest_number(number_list):
    # Base case: if the list has a single element, return that element
    if len(number_list) == 1:
        return number_list[0]
    else:
        # Recursive case: compare first element with largest integer
        return max(number_list[0], largest_number(number_list[1:]))

# Test case
print(largest_number([1, 5, 2, 6, 10, 51, 16]))