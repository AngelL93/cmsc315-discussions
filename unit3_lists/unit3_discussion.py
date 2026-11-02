"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """

    "Existing elements are moved to the right depending on where the value was inserted"
    "Performance may vary depending on where the value is inserted."
    "The closer you insert at the beginning, the longer it takes because the more values that will need to be moved"
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """

    "Checks for valid index"
    if 0 <= index < len(lst):
        "removes and returns the value at the index"
        return lst.pop(index)

    "Returns None if index is invalid"
    return None

    "Index validation is important because it ensures we remove the correct index from the list"
    "Safe deletion is important to prevent removing the wrong index and prevent errors as well"


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """

    "Checks each element in the list for the correct value"
    for index in range(len(lst)):
        if lst[index] == value:
            return index

    "Return -1 if value is not found"
    return -1

    "This is a linear search because it searches each element one by one until it finds the value"


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.")

    "Lists containing several values and displays the list"
    numbers = [10,20,30,40]
    print("List 1:", numbers)

    "Inserts value 5 to the beginning of the list and displays the updated list"
    insert_at(numbers, 0, 5)
    print("The beginning:", numbers)

    "Inserts value 15 in the middle at index 2 and displays the updated list"
    insert_at(numbers, 2, 15)
    print("The middle:", numbers)

    "Inserts value 50 at the end of the list and displays the updated list"
    insert_at(numbers, len(numbers), 50)
    print("The end:", numbers)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")

    "List for deleting indexes"
    numbers = [2,4,6,8]
    print("List 2:", numbers)

    "Delete from the beginning"
    removed = delete_at(numbers, 0)
    print("Remove:", removed)
    print("Updated list:", numbers)

    "Delete from the middle"
    removed = delete_at(numbers, 1)
    print("Remove:", removed)
    print("Updated list:", numbers)

    "Delete from the end"
    removed = delete_at(numbers, len(numbers) -1)
    print("Remove:", removed)
    print("Updated list:", numbers)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")

    "List for searching indexes."
    numbers = [50, 100, 150, 200]
    print("List 3:", numbers)

    "Search for a value that exists."
    print("Search for 100:", search_value(numbers, 100))

    "Search for a value that does not exist."
    print("Search for 25:", search_value(numbers, 25))


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")


    "Delete using an invalid index"
    numbers = [1000, 2000, 3000, 4000]
    print("Invalid deletion:", delete_at(numbers, 1000))

    "Search for a missing value"
    print("missing value:", search_value(numbers, 999))

    "Insert into the empty list"
    numbers = []
    insert_at(numbers, 0, 100)
    print("Insert into the empty list:", numbers)

    "Delete from the empty list"
    numbers = []
    print("Delete from the empty list:", delete_at(numbers, 0))


    print("\n=== REAL-WORLD SCENARIO ===")

    "List of customers"
    customers = ["John", "Mary", "David"]
    print("List:", ",".join(customers))


    "Add Sarah to the list"
    insert_at(customers, 1, "Sarah")
    print("Add Sarah to the list:", ",".join(customers))

    "Remove Mary from list"
    delete_at(customers, 2)
    print("Remove Mary from the list:", ",".join(customers))

    "Search for customer in list"
    print("Search for Angel:", search_value(customers, "Angel"))


if __name__ == "__main__":
    main()