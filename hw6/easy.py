def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total

# Time Complexity: O(n)
# Where n is the number of elements in the array.
# We visit each element exactly once.

if __name__ == "__main__":
    test_data = [3, 1, 4, 1, 5, 9]
    print("Input:", test_data)
    print("Sum of elements:", sum_array(test_data))