def max_difference(arr):
    if len(arr) < 2:
        return 0

    min_val = arr[0]
    max_diff = 0
    for num in arr[1:]:
        if num < min_val:
            min_val = num
        else:
            diff = num - min_val
            if diff > max_diff:
                max_diff = diff

    return max_diff

# Time Complexity: O(n)
# We update min_val and max_diff in a single traversal of the array.

if __name__ == "__main__":
    test_data = [2, 8, 3, 1, 10, 4]
    print("Input:", test_data)
    print("Maximum difference:", max_difference(test_data))