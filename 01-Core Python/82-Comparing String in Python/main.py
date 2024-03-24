'''
In Python, you can compare strings using comparison operators such as ==, !=, <, >, <=, and >=. These operators allow you to determine the relative order of strings based on their lexicographical order (i.e., dictionary order).

Here's how you can use comparison operators to compare strings:
'''

# Define two strings
string1 = "apple"
string2 = "banana"

# Comparing strings using comparison operators
print(string1 == string2)  # Output: False (string1 is not equal to string2)
print(string1 != string2)  # Output: True (string1 is not equal to string2)
print(string1 < string2)   # Output: True (string1 comes before string2 in lexicographical order)
print(string1 > string2)   # Output: False (string1 comes after string2 in lexicographical order)
print(string1 <= string2)  # Output: True (string1 comes before or is equal to string2)
print(string1 >= string2)  # Output: False (string1 comes after or is equal to string2)

'''In this example:

We define two strings, "apple" and "banana".
We compare the strings using different comparison operators:
== checks for equality.
!= checks for inequality.
< checks if the first string comes before the second string in lexicographical order.
> checks if the first string comes after the second string in lexicographical order.
<= checks if the first string comes before or is equal to the second string.
>= checks if the first string comes after or is equal to the second string.
String comparison in Python is case-sensitive. This means that uppercase letters are considered different from lowercase letters when comparing strings. For example, "apple" and "Apple" are considered different strings when using comparison operators. If you want case-insensitive comparison, you can convert strings to lowercase (or uppercase) using the lower() (or upper()) method before comparing them.'''