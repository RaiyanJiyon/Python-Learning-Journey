'''
Union (union() or | operator): Returns a new set containing all the unique elements present in both sets.
'''

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)
# or
union_set = set1 | set2

print(union_set)  # Output: {1, 2, 3, 4, 5}


'''
Intersection (intersection() or & operator): Returns a new set containing only the elements that are present in both sets.
'''

set1 = {1, 2, 3}
set2 = {3, 4, 5}

intersection_set = set1.intersection(set2)
# or
intersection_set = set1 & set2

print(intersection_set)  # Output: {3}


'''
Difference (difference() or - operator): Returns a new set containing elements that are present in the first set but not in the second set.
'''

set1 = {1, 2, 3}
set2 = {3, 4, 5}

difference_set = set1.difference(set2)
# or
difference_set = set1 - set2

print(difference_set)  # Output: {1, 2}


'''
Symmetric Difference (symmetric_difference() or ^ operator): Returns a new set containing elements that are present in either of the sets, but not in both.
'''

set1 = {1, 2, 3}
set2 = {3, 4, 5}

symmetric_difference_set = set1.symmetric_difference(set2)
# or
symmetric_difference_set = set1 ^ set2

print(symmetric_difference_set)  # Output: {1, 2, 4, 5}


'''
Subset (issubset()): Checks whether the set is a subset of another set.
'''

set1 = {1, 2, 3}
set2 = {1, 2}

print(set1.issuperset(set2))  # Output: True


'''These are some of the essential set methods in Python that allow you to perform various operations on sets efficiently.'''