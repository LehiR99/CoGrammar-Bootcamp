def binary_search(arr, target):
    """
    Function to find a number within a sorted list.
    """
    left_index = 0
    right_index = len(arr) - 1

    # The search loop
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        if arr[mid_index] == target:
            return mid_index
        elif arr[mid_index] < target:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1

# The original list
original_list = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
# Sorting the list using a simple sorting method
sorted_list = original_list[:]
for current_index in range(1, len(sorted_list)):
    current_element = sorted_list[current_index]
    position = current_index - 1
    while position >= 0 and sorted_list[position] > current_element:
        sorted_list[position + 1] = sorted_list[position]
        position -= 1
    sorted_list[position + 1] = current_element

# Using the binary search to locate the number 9
# Binary search was chosen as it's efficient for ordered lists,
# quickly narrowing down the search space, like going through a book
index = binary_search(sorted_list, 9)
if index != -1:
    print("Found 9 at index:", index)
else:
    print("Couldn't find 9 in the list.")

def interpolation_search(arr, target):
    """
    Function to find a number within a sorted list using interpolation.
    """
    left_index = 0
    right_index = len(arr) - 1

    # The interpolation search loop
    while left_index <= right_index and arr[left_index] <= target <= arr[right_index]:
        # Interpolation formula for position
        mid_index = left_index + ((target - arr[left_index]) * (right_index - left_index)) // (arr[right_index] - arr[left_index])

        if arr[mid_index] == target:
            return mid_index
        elif arr[mid_index] < target:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1

# Using interpolation search to find 9
# Interpolation search is good when you have an idea where
# things are and they're evenly spaced out, like in a dictionary.
index = interpolation_search(sorted_list, 9)
if index != -1:
    print("Found 9 at index:", index)
else:
    print("Couldn't find 9 in the list.")
