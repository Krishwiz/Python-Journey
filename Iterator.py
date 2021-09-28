# from _typeshed import Self


# a = ["hey", "bro", "you're","awesome"]

# for i in a:
#     print(i)

# Implementation of interator using class

class RemoteControl():
    def __init__(self):
        self.channels = ["Sun", "KTv", "Jaya"]
        self.index = -1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration
        
        return self.channels[self.index]
    

r = RemoteControl()

print(next(r))