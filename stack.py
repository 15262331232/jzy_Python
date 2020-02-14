class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,item):
        self.stack.insert(0,item)

    def top(self):
        try:
            return self.stack[0]
        except IndexError:
            return None

    def pop(self):
        try:
            self.stack.pop(0)
        except IndexError:
            raise Exception("The stack is empty!")

