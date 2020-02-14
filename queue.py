class Queue:
    def __init__(self):
        self.queue=[]

    def push(self,item):
        self.queue.append(item)

    def front(self):
        try:
            return self.queue[0]
        except IndexError:
            return None

    def pop(self):
        try:
            self.queue.pop(0)
        except IndexError:
            raise Exception("The queue is empty!")

