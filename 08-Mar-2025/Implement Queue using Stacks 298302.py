# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.stack_add = []
        self.stack_remove = []

    def push(self, x: int) -> None:
        self.stack_add.append(x)

    def pop(self) -> int:
        if not self.stack_remove:
            while self.stack_add:
                self.stack_remove.append(self.stack_add.pop())
        return self.stack_remove.pop() if self.stack_remove else -1

    def peek(self) -> int:
        if not self.stack_remove:
            while self.stack_add:
                self.stack_remove.append(self.stack_add.pop())
        return self.stack_remove[-1] if self.stack_remove else -1

    def empty(self) -> bool:
        return not self.stack_add and not self.stack_remove



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()