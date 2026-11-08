"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
            self.value = value
            self.left = None
            self.right = None



class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None


    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # Larger values for right and smaller values go left to help find the correct spot for new values
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        if node is None:
            return Node(value)

        if value < node.value:
            # Small values go to the left.
            node.left = self._insert_recursive(node.left, value)

        elif value > node.value:
            # Larger values go to the right:
            node.right = self._insert_recursive(node.right, value)

        return node


    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # BST search us often faster than linear search
        # because it can skip entire branches
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        if node is None:
            return False

        if value == node.value:
            return True

        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """

        # Smaller values are left and larger are right. They go through the BST and sort according to size
        if node is not None:
            # Visit the left subtree first
            self._inorder_recursive(node.left, values)
            # Add the current node to the list
            values.append(node.value)
            # Visit the right subtree last
            self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    print("TODO: Create a BST and insert multiple values.")

    # Binary Search Tree object
    bst = BST()

    # Values for the BST object
    values = [50, 30, 70, 20, 40, 60, 80]

    # A BST reduces the search space by comparing values
    # Smaller value go left and the larger goes right
    # Preventing searching every node in the BST
    for value in values:
        bst.insert(value)

    # Displays the values inserted
    print("Inserted values:", values)

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")

    # In-order traversal visits left, root, the right
    # Since smaller values are in the left and larger values are on the right,
    # the resuls are sorted
    sorted_values = bst.inorder()

    # Displays teh in-order traversal
    print("In-order traversal:", sorted_values)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")

    # These values exist in the tree, so they return True
    print("Search for 30:", bst.search(30))
    print("Search for 70:", bst.search(70))

    # These values are not in the tree, so they return False
    print("Search for 25:", bst.search(25))
    print("Search for 90:", bst.search(90))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")

    # Create an empty BST
    empty_bst = BST()

    # Search an empty tree returns False because there are no nodes to search
    print("Search empty tree:", empty_bst.search(50))

    print("\n=== REAL-WORLD SCENARIO ===")

    # Create a BST to organize property prices.
    property_bst = BST()

    # List of property prices in thousands.
    property_prices = [300, 250, 400, 200, 275, 350, 450]

    # Insert each property price into the tree.
    for price in property_prices:
        property_bst.insert(price)

    # Display the original property prices.
    print("Property prices:", property_prices)

    # Display the prices from lowest to highest.
    print("Sorted property prices:", property_bst.inorder())

    # Search for a property priced at $275,000.
    print("Property at $275,000:", property_bst.search(275))

    # Search for a property priced at $500,000.
    print("Property at $500,000:", property_bst.search(500))


if __name__ == "__main__":
    main()