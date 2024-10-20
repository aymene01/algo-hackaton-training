from data_structures.stack import MinStack

stack = MinStack()
stack.push(10)
stack.push(20)
stack.push(1)
stack.push(19)
stack.push(13)

print(stack.get_min())
print(stack.peek())
print(stack.pop())
print(stack.get_max())

