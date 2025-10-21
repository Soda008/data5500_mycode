def second_largest(arr):
    if len(arr) < 2:
        return None

    largest = second = float('-inf')
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif largest > num > second:
            second = num

    return second

# Time Complexity: O(n)
# We make one pass through the list, comparing each element only once.

if __name__ == "__main__":
    test_data = [7, 3, 9, 1, 9, 5]
    print("Input:", test_data)
    print("Second largest:", second_largest(test_data))