Class Count:
    def __init__(self, start, end):
        self.start = start
        self.end =  end

    def __iter__(self):
        return self# This makes it an interator

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            num = self.current
            self.current += 1
            return num


counter = Count(1, 3)

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
