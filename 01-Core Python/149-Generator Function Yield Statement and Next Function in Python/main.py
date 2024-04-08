'''
In Python, a generator function is a special type of function that allows you to generate a sequence of values lazily, meaning that it produces values one at a time as they are needed, rather than generating them all at once and storing them in memory. The key feature of a generator function is the yield statement, which temporarily suspends the function's execution and returns a value to the caller, but unlike return, it allows the function to resume where it left off when called again.

Here's a simple example of a generator function:
'''

def my_generator():
    yield 1
    yield 2
    yield 3


# You can create a generator object by calling the generator function:
gen = my_generator()

'''
You can then retrieve values from the generator using the next() function or by iterating over it with a loop:
'''

print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3

'''
Once all values have been yielded, if you try to call next() again, it will raise a StopIteration exception.
'''

# print(next(gen))  # Raises StopIteration

'''Alternatively, you can iterate over the generator using a loop:'''

for value in gen:
    print(value)


'''The yield statement is what makes this function a generator. When next() is called, the function executes until it encounters a yield statement, at which point it returns the value after the yield and suspends execution. When next() is called again, execution resumes from where it left off until the next yield statement or until the function returns.'''
