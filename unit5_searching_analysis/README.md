# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:


1. What concepts or skills did you learn while completing this assignment?

I learned more about how linear search and binary search work and why their performance is different. 
Linear search goes through each value one at a time, while binary search divides the search area in half. 
I also learned how the size of a dataset can affect how efficiently a program runs.

2. What challenges did you encounter, and how did you overcome them?

One challenge was understanding how binary search knows which half of the list to search next. 
I had to go through the code and understand what each variable was doing. 
Testing smaller lists helped me see how the algorithm works and why the indexes change.

3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.

Linear search is useful for smaller lists or lists that aren't sorted. 
Binary search is better for larger sorted lists because it doesn't need to check every value. 
The real-world scenario, searching through a large list of home prices would be faster with binary search if the prices were already sorted,
but it can add more time if you were to sort the list.