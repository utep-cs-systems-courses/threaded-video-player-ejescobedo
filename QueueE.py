class QueueE:

    size = 0
    queue = []
    
    def __init__(self, capacity = 10):
        self.capacity = capacity

    def enqueue(self, item):
        if self.size < 10:
            print("here")
            self.queue.append(item)
            self.size = self.size + 1

    def dequeue(self):
        if self.size > 0:
            self.size = self.size - 1
        return self.queue.pop(0)

    def peek(self):

        return self.queue[0]

if __name__ == "__main__":
    currQ = QueueE(10)

    currQ.enqueue("a")
    currQ.enqueue("b")
    currQ.enqueue("c")
    print(currQ.queue)
    print(currQ.peek())
    currQ.dequeue()
    print(currQ.peek())
    currQ.dequeue()
    print(currQ.peek())