def list_demo():
    print("--- List Demo ---")
    my_list = [1, 2, 3, 4, 5]
    print("Original List:", my_list)
    
    print("First element:", my_list[0])
    
    my_list.append(6)
    print("After append:", my_list)
    
    my_list.remove(3)
    print("After remove 3:", my_list)
    print()

def set_demo():
    print("--- Set Demo ---")
    my_set = {1, 2, 3, 3, 4}
    print("Original Set (duplicates removed):", my_set)
    
    my_set.add(5)
    print("After add 5:", my_set)
    
    my_set.discard(2)
    print("After discard 2:", my_set)
    print()

def stack_demo():
    print("--- Stack Demo (LIFO) ---")
    stack = []
    
    stack.append(1)
    stack.append(2)
    stack.append(3)
    print("Stack after pushes:", stack)
    
    popped = stack.pop()
    print("Popped element:", popped)
    print("Stack after pop:", stack)
    print()

def queue_demo():
    from collections import deque
    print("--- Queue Demo (FIFO) ---")
    queue = deque()

    queue.append(1)
    queue.append(2)
    queue.append(3)
    print("Queue after enqueues:", list(queue))
    
    dequeued = queue.popleft()
    print("Dequeued element:", dequeued)
    print("Queue after dequeue:", list(queue))
    print()

if __name__ == "__main__":
    list_demo()
    set_demo()
    stack_demo()
    queue_demo()
