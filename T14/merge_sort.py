def merge_sort_by_length(arr):
    """
    Sorts a list of strings by their lengths using the merge sort algorithm.

    Args:
    arr (list): The list of strings to be sorted.

    Returns:
    None: The original list is sorted in-place.
    """
    if len(arr) > 1:
        # Splitting the list into two halves
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Sorting each half recursively
        merge_sort_by_length(left_half)
        merge_sort_by_length(right_half)

        # Merging the sorted halves
        left_index = right_index = arr_index = 0

        while left_index < len(left_half) and right_index < len(right_half):
            # Comparing string lengths
            if len(left_half[left_index]) > len(right_half[right_index]):
                arr[arr_index] = left_half[left_index]
                left_index += 1
            else:
                arr[arr_index] = right_half[right_index]
                right_index += 1
            arr_index += 1

        # Copying remaining elements of left_half
        while left_index < len(left_half):
            arr[arr_index] = left_half[left_index]
            left_index += 1
            arr_index += 1

        # Copying remaining elements of right_half
        while right_index < len(right_half):
            arr[arr_index] = right_half[right_index]
            right_index += 1
            arr_index += 1


if __name__ == "__main__":
    # Example lists to sort
    list1 = ["mountain", "ocean", "forest", "river", "canyon", "valley", "desert", "plateau", "volcano", "glacier"]
    list2 = ["dog", "cat", "horse", "rabbit", "hamster", "turtle", "goldfish", "parrot", "snake", "lizard"]
    list3 = ["car", "bicycle", "motorcycle", "truck", "bus", "train", "boat", "plane", "helicopter", "rocket"]

    # Sorting each list by string length
    merge_sort_by_length(list1)
    merge_sort_by_length(list2)
    merge_sort_by_length(list3)

    # Displaying the sorted lists
    print("Here are the lists, now sorted by length:")
    print("List 1:", list1)
    print("List 2:", list2)
    print("List 3:", list3)

