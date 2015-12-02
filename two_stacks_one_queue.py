class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        if not self.items: return None
        return self.items[len(self.items)-1]

# Queue implemented with 2 stacks
class SpecialQueue(Stack):
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, item):
        self.in_stack.push(item)

    def dequeue(self):
        if not self.out_stack.isEmpty():
            return self.out_stack.pop()
        while not self.in_stack.isEmpty():
            self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()

class MaxStack(Stack):
    def __init__(self):
        self.items = []
        self.max_vals = Stack()

    def push(self, item):
        self.items.append(item)
        if self.max_vals.peek() < item: 
            self.max_vals.push(item)

    def pop(self):
        if self.max_vals == self.peek(): 
            self.max_vals.pop()
        return self.items.pop()

    def get_max(self):
        return self.max_vals.peek()


if __name__ == "__main__":
    sq = SpecialQueue()
    sq.enqueue(8)
    sq.enqueue(2)
    
    ms = MaxStack()
    ms.push(1)
    ms.push(7)
    ms.push(8)
    ms.push(3)
    print ms.get_max()
    