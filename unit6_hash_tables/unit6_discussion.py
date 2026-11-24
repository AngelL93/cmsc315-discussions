"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.


    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")

    # Create a dictionary with five students and grades and include each name key and value.
    # Hashing is used to find stored keys.
    student_grades = {"John": 90, "Mary": 85, "Alex": 92, "Sarah": 88, "David": 95}

    print("Student grades:", ", " .join(student_grades))

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")

    # Use keys to quicky find student grades
    print("John's grades:", student_grades["John"])
    print("Mary's grade:", student_grades["Mary"])

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")

    # Display grades before making changes
    print("Before update:", ", " .join(student_grades))

    # Change John's grade from 90 to 98
    student_grades["John"] = 98

    # Display grade after update.
    print("After update:", ", " .join(student_grades))

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")

    # Display dictionary before deletion of a student.
    print("Before deletion:", ", " .join(student_grades))

    # Remove David from the dictionary
    del student_grades["David"]

    # Display dictionary after deletion
    print("After deletion:", ", " .join(student_grades))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")

    #1 Look up a student who does not exist
    print("Mike's grade:", student_grades.get("Mike", "Not found"))

    #2 Trying to delete a missing student
    removed = student_grades.pop("Mike", "Student not found" )
    print("Delete Mike:", removed)

    print("\n=== REAL-WORLD SCENARIO ===")

    # A teacher uses a dictionary to track grades to quickly find or update them
    for name, grade in student_grades.items():
        print(name, "has a grade", grade)


if __name__ == "__main__":
    main()