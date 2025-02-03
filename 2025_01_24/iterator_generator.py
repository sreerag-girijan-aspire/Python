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
my_generator_obj = my_generator(3, 10)
for i in range(5):
    print(my_generator_obj.__next__())

# An iterator in Python is an object that allows you to traverse through all the elements of a collection,
# such as a list or a tuple, one element at a time. It implements two special methods: __iter__() and __next__().
# The __iter__() method returns the iterator object itself, and the __next__() method returns the next element
# in the sequence. When there are no more elements to return, __next__() raises a StopIteration exception to
# signal that the iteration is complete.

# A generator in Python is a special type of iterator that allows you to iterate over a sequence of values.
# Unlike a regular iterator, a generator is defined using a function rather than a class. The function uses
# the 'yield' keyword to return values one at a time, pausing the function's state between each yield.
# When the generator's __next__() method is called, the function resumes execution from where it left off,
# continuing until it encounters another 'yield' statement or reaches the end of the function. Generators
# provide a convenient way to create iterators without the need to implement the __iter__() and __next__()
# methods manually.
