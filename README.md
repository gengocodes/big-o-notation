# Data Structures and Algorithms

This repository contains Python demos for common **data structures** and **Big O concepts**, including lists, sets, stacks, queues, hash tables, graphs, and heaps. It also provides examples for basic time complexities like O(1), O(n), O(log n), O(n²), common sorting and searching algorithms, and algorithmic strategies like divide & conquer, recursion, and greedy algorithms.

---

## Big O Notation Examples

| Concept  | Use Case                 | Time Complexity | Space Complexity |
| -------- | ------------------------ | --------------- | ---------------- |
| O(1)     | Access a single element  | Constant        | Constant         |
| O(n)     | Iterating through a list | Linear          | Linear           |
| O(log n) | Binary search            | Logarithmic     | Constant         |
| O(n²)    | Nested loops             | Quadratic       | Linear           |

---

## Data Structures

| Data Structure | Use Case                                  | Time Complexity (Average)                       | Space Complexity |
| -------------- | ----------------------------------------- | ----------------------------------------------- | ---------------- |
| List           | Ordered collection, allow duplicates      | Access: O(1), Search: O(n), Insert/Delete: O(n) | O(n)             |
| Set            | Unique collection, fast membership check  | Add/Remove/Lookup: O(1)                         | O(n)             |
| Stack (LIFO)   | Undo functionality, expression evaluation | Push/Pop: O(1)                                  | O(n)             |
| Queue (FIFO)   | Task scheduling, buffering                | Enqueue/Dequeue: O(1)                           | O(n)             |
| Hash Table     | Fast key-value lookup                     | Insert/Search/Delete: O(1)                      | O(n)             |
| Graph          | Represent relationships, networks         | BFS/DFS: O(V+E)                                 | O(V+E)           |
| Heap           | Priority queue, top-k problems            | Insert/Delete: O(log n), Peek: O(1)             | O(n)             |

---

## Sorting Algorithms

| Algorithm       | Time Complexity (Best) | Time Complexity (Average) | Time Complexity (Worst) | Space Complexity |
| --------------- | -------------------- | ------------------------ | ---------------------- | ---------------- |
| Selection Sort  | O(n²)                | O(n²)                    | O(n²)                  | O(1)             |
| Insertion Sort  | O(n)                 | O(n²)                    | O(n²)                  | O(1)             |
| Quick Sort      | O(n log n)           | O(n log n)                | O(n²)                  | O(n)             |

---

## Searching Algorithms

| Algorithm       | Time Complexity (Best) | Time Complexity (Average) | Time Complexity (Worst) | Space Complexity |
| --------------- | -------------------- | ------------------------ | ---------------------- | ---------------- |
| Linear Search   | O(1)                 | O(n)                     | O(n)                   | O(1)             |
| Binary Search   | O(1)                 | O(log n)                 | O(log n)               | O(1)             |

---

## Algorithmic Strategies

| Strategy              | Example Algorithm        | Use Case / Notes |
| --------------------- | ----------------------- | ---------------- |
| Divide & Conquer      | Merge Sort              | Break problem into subproblems, solve individually, and combine results. |
| Recursion             | Factorial               | Function calls itself to solve smaller instances of a problem. |
| Greedy Algorithm      | Coin Change (min coins) | Make the locally optimal choice at each step to find a global optimum. |

This repository has been created to keep notes of my learning in the Meta Coding Interview Preparation Certification course.