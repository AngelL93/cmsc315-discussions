"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """

    # Go through the list from beginning to end
    for i in range(len(lst)):

        # Check if the current number is our target
        if lst[i] == target:
            return i

    # Return -1 if the number was not found
    return -1

    # Linear search is 0(n) because it may need to check every number in the list.

def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    # Set the beginning and end of the list
    left = 0
    right = len(lst) - 1

    # Keep searching while there are numbers left
    while left <= right:

        # Find the middle index
        mid = (left + right) // 2

        # Check if the middle number is our target
        if lst[mid] == target:
            return mid

        # If target is bigger, search the right half
        elif lst[mid] < target:
            left = mid + 1

        # If target is bigger, search the left half
        else:
            right = mid - 1

        # Return -1 if the target was not found
        # Binary search is 0(log n) because it removes half the remaining numbers each time
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    print("TODO: Create a small dataset and test both searches.")

    # Create a small sorted dataset
    small_list = [2, 4, 6, 8, 10]

    print("Small list:", small_list)

    # Test a number that exists in the list
    print("Linear search for 6:", linear_search(small_list, 6))

    print("Binary search for 6:", binary_search(small_list, 6))

    # Test a number that does not exist
    print("Linear search for 7:", linear_search(small_list, 7))

    print("Binary search for 7:", binary_search(small_list, 7))


    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    print("TODO: Create a larger dataset and compare results.")

    # Create a sorted list with 10,000 numbers
    large_list = list(range(1, 10001))

    # Search for the last number
    print("Linear search for 10000:", linear_search(large_list, 10000))

    print("Binary search for 10000:", binary_search(large_list, 10000))


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Demonstrating that an empty list return -1
    # Edge Case 1

    # Empty list
    empty_list = []

    print("Linear search empty list:", linear_search(empty_list, 5))

    print("Binary search empty list:", binary_search(empty_list, 5))

    # Return 0 because 10 is at the index 0
    # Edge Case 2

    # Empty list
    single_list = [5]

    print("Linear search list:", linear_search(single_list, 5))


if __name__ == "__main__":
    main()