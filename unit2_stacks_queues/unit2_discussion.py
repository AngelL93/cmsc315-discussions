"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.stack = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # This operation supports LIFO because it adds each new value to the end of the list, which is the top
        self.stack.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty
        # This returns the value None if stack is empty to prevent an error
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Shows the what the top value is without removing it
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.stack) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.queue = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # This operation supports FIFO because it adds the first value to the queue, so the first value added is the first removed
        self.queue.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        # Returns None if the queue is empty to prevent an error.
        if self.is_empty():
            return None
        return self.queue.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # Shows the first value without removing it
        if self.is_empty():
            return None
        return self.queue[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.queue) == 0

def main():

    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.

    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


print("\n=== STACK DEMO ===")
print("TODO: Create a Stack object, demonstrate LIFO behavior,")

stack = Stack()

stack.push(5)
stack.push(1)
stack.push(9)
stack.push(6)

print("Print stack:", stack.stack)
print()
print("Show which value is last in:", stack.peek())
print("Show and remove value that was last in:", stack.pop())
print("Show and remove value that was last in:", stack.pop())
print("Is the stack empty?:", stack.is_empty())
print("Show and remove value that was last in:", stack.pop())
print()
print("      Test popping from an empty stack.")
print("Show and remove value that was last in:", stack.pop())
print("Is the stack empty?:", stack.is_empty())
print("Show and remove value that was last in:", stack.pop())

# peek used on an empty stack returns the value None
print()
print("      Test peeking at an empty stack.")
print("Show which value is last in:", stack.peek())

print()
print("      Verify a single-item stack becomes empty after removal.")
one_stack = Stack()

one_stack.push(58)

print()
print(one_stack.stack)
print("Show and remove value that was last in:", one_stack.pop())
print("Is the stack empty?:", one_stack.is_empty())

# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

print("\n=== QUEUE DEMO ===")

print("TODO: Create a Queue object, demonstrate FIFO behavior")
queue = Queue()

queue.enqueue(56)
queue.enqueue(40)
queue.enqueue(91)
queue.enqueue(18)

print("Print queue: ", queue.queue)

print()
print("      Test dequeuing from an empty queue.")
print("Show which value is in front:", queue.front())
print("Remove value that is in front:", queue.dequeue())
print("Show new queue", list(queue.queue))
print("Remove value that is in front:", queue.dequeue())
print("Is the queue empty?:", queue.is_empty())
print("Remove value that is in front:", queue.dequeue())

# front used on an empty queue returns the value None
print()
print("      Test using front on an empty queue.")
print("Remove value that is in front:", queue.dequeue())
print("Is the queue empty?:", queue.is_empty())

print()
print("      Test viewing the front of an empty queue.")
print("      Verify a single-item queue becomes empty after removal.")
one_queue = Queue()

one_queue.enqueue(100)

print()
print(one_queue.queue)
print("Remove and return value that is in front:", one_queue.dequeue())
print("Is the queue empty?:", one_queue.is_empty())

print()
print()
print("\n=== REAL-LIFE SCENARIO ===")

print("Names of customers in a line at Starbucks")
queue = Queue()

queue.enqueue("Rachael")
queue.enqueue("Angel")
queue.enqueue("Allen")
queue.enqueue("Luke")

print("Print queue: ", queue.queue)

print()
print("Show who is in front of the line:", queue.front())
print("Customers orders and is removed from line", queue.dequeue())
print("Show new queue", list(queue.queue))
print("Show who is in front of the line:", queue.front())
print("Remove value that is in front:", queue.dequeue())
print("Is the queue empty?:", queue.is_empty())
print("Show who is in front of the line:", queue.front())
print("Remove value that is in front:", queue.dequeue())
print("Show who is in front of the line:", queue.front())
print("Remove value that is in front:", queue.dequeue())
print("Is the stack empty?:", queue.is_empty())
print("Remove value that is in front:", queue.dequeue())
print("Show new queue", list(queue.queue))

if __name__ == "__main__":
    main()
