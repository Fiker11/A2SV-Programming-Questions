class MyStack:
    def __init__(self):
        self.queue = []  

    def push(self, x: int) -> None:
        
        temp = []
        while self.queue:
            temp.append(self.queue.pop(0))
        self.queue.append(x)

        while temp:
            self.queue.append(temp.pop(0))

    def pop(self) -> int:
        if not self.empty():
            return self.queue.pop(0)  
        else:
            raise IndexError("Stack is empty") 
    def top(self) -> int:
        if not self.empty():
            return self.queue[0]
        else:
            raise IndexError("Stack is empty")  
    def empty(self) -> bool:
        return not self.queue  

