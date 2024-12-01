from typing import List


class Stack:
    def __init__(self):
        self.data: List[str] = []

    def push(self, element: str) -> None:
        self.data.append(element)

    def pop(self) -> str:
        return self.data.pop()

    def top(self) -> str:
        return self.data[-1]

    def is_empty(self) -> bool:
        return not self.data

    def __str__(self):
        reversed_data = reversed(self.data)
        return f"[{', '.join(reversed_data)}]"


stack = Stack()
print(stack.is_empty())
stack.push("apple")
stack.push("carrot")
print(stack.top())
print(stack.push("cucumber"))
print(stack.top())
print(stack.is_empty())
print(stack.pop())
print(stack)
