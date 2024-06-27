numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]


# Sorting a Tuple:
letters = ('b', 'd', 'c', 'a')
sorted_letters = sorted(letters)
print(sorted_letters)  # Output: ['a', 'b', 'c', 'd']


# Sorting a String:
word = "hello"
sorted_word = sorted(word)
print(sorted_word)  # Output: ['e', 'h', 'l', 'l', 'o']


# Sorting with Custom Key Function:
words = ['banana', 'apple', 'orange', 'grape']
sorted_words = sorted(words, key=len)
print(sorted_words)  # Output: ['apple', 'grape', 'banana', 'orange']


# Sorting in Reverse Order:

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)  # Output: [9, 6, 5, 5, 4, 3, 3, 2, 1, 1]