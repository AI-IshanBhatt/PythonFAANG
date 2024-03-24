
# You can use deque's popleft and append functions only
from collections import deque


class StackWithQueue:

    def __init__(self):
        self.queue = deque()

    def push(self, item):
        self.queue.append(item)

    def pop(self) -> int:
        # We popleft N-1 elements and add them to the back of the queue
        # Then we return the Nth element which will be at front after all those operations

        N = len(self.queue)
        for i in range(N-1):
            self.queue.append(self.queue.popleft())
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[-1]


if __name__ == "__main__":
    s = StackWithQueue()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)

    print(s.pop())
    print(s.pop())
    print(s.queue)
