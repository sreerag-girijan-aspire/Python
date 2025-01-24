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

def my_generator(start, end):
    iterator = MyIterator(start, end)
    for value in iterator:
        yield value

# Example usage
for value in my_generator(1, 10):
    print(value)


# Example usage 2
print()
my_generator_obj=my_generator(3,10)
for i in range(5):
    print(my_generator_obj.__next__())
