
class QueueWithStack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def top(self) -> int:
        return self.stack[0]

    def is_empty(self):
        return not self.stack

    def pop(self) -> int:
        current_value = self.stack.pop()
        if not self.stack:
            return current_value  # In this call we are not allowing to current_value to be pushed again

        item = self.pop()
        self.push(current_value)
        return item


if __name__ == "__main__":
    q = QueueWithStack()
    q.push(1)
    q.push(2)
    q.push(3)

    print(q.stack)
    print(q.pop())
    print(q.stack)
    print(q.top())
    print(q.is_empty())
    print(q.pop())
    print(q.pop())
    print(q.is_empty())