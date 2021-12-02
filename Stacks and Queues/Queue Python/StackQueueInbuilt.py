
import queue



# inbuilt stack as List.

# s = [1, 2, 3]
# s.append(4)
# s.append(5)

# print(s.pop())
# print(s.pop())


# inbuilt queue.

q = queue.Queue()

q.put(1)
q.put(2)
q.put(3)
q.put(4)

while not q.empty():
	print(q.get())      # Output will follow  FIFO property (First In First Out)


# inbuilt stack as queue.

# q = queue.LifoQueue()

# q.put(1)
# q.put(2)
# q.put(3)

# while not q.empty():
# 	print(q.get())      # Output will follow LIFO property (Last In First Out).