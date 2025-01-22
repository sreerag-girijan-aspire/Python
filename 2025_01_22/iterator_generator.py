# Iterator example
class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

# Using the iterator
iterator = MyIterator(1, 5)
for value in iterator:
    print(value)

# Generator example
def my_generator(start, end):
    current = start
    while current < end:
        yield current
        current += 1

# Using the generator
for value in my_generator(1, 5):
    print(value)