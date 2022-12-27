from collections import deque

deque_int = deque((1, 2, 3, 4))
print(deque_int)

deque_int.append(5)
deque_int.appendleft(0)
print(deque_int)
print("NEVER APPEND TO LEFT OF LIST it is O(N)")

deque_int.extendleft([-1,-2])
print(deque_int)

x = deque_int.popleft()
y = deque_int.pop()

print(x)
print(y)
print(deque_int)

deque_int.extend(range(10,15))
print(deque_int)
print()

print("DEQUE CAN BE INDEXED BY 0 , -1 => USE THEM AS top(), peek() methods")
print(f"Without removing top from left TO BE USED IN QUEUE {deque_int[0]}")
print(f"Without removing top from right TO BE USED IN STACK {deque_int[1]}")

print("Limiting the Maximum Number of Items: maxlen")
another_queue = deque(maxlen=5)
another_queue.extend(range(1,6))
print(another_queue)
another_queue.appendleft(0)  # Will remove element from right side
print(another_queue)
another_queue.append(6)  # Will remove element from left side
print(another_queue)
print()

print("Rotating the deque")
another_queue.rotate(1)
print(another_queue)
another_queue.rotate(-2)
print(another_queue)