# ------------------------------------------------------------------------

# Lab 1
# Problem 1
# 1. Create a list called my_list with the values [1, 5, 'apple', 20.5].
def make_list(my_list: list[any]) -> list[any]:
    my_list = [1, 5, 'apple', 20.5]
    print(my_list)

make_list(make_list)

# 2. Using indexing, print the value 'apple' from my_list.
def find_apple(my_list: list[int]) -> list[int]:
    my_list = [1, 5, 'apple', 20.5]
    print(my_list[2])

find_apple(find_apple)

# 3. Add the value 10 to the end of my_list using the append() method. Print the updated list.
def add_to_list(my_list: list[int]) -> list[int]:
    my_list = [1, 5, 'apple', 20.5]
    my_list.append(10)
    print (my_list) 

add_to_list(add_to_list)

# 4. Remove the value 20.5 from my_list using the remove() method. Print the updated list.
def take_off_list(my_list: list[int]) -> list[int]:
    my_list = [1, 5, 'apple', 20.5, 10]
    my_list.remove(20.5)
    print(my_list)

take_off_list(take_off_list)

# 5. Reverse the order of the elements in my_list using a method. Print the reversed list.
def reverse_list(my_list: list[int]) -> list[int]:
    my_list = [1, 5, 'apple', 10]
    my_list.reverse()
    print(my_list)

reverse_list(reverse_list)

# Problem 2
# 1. Create a dictionary called person with keys 'name', 'age', 'job' and values 'John', 30, 'teacher'.
def make_dictionary(person):
    person = {'name': 'John', 'age': 30, 'job': 'teacher'}
    print(person)

make_dictionary(make_dictionary)

# 2. Print the value corresponding to the 'job' key.
def find_job(person):
    person = {'name': 'John', 'age': 30, 'job': 'teacher'}
    print(person['job'])

find_job(find_job)

# 3. Add a new key-value pair: 'city': 'Paris' to the person dictionary. Print the updated dictionary.
def add_place(person):
    person = {'name': 'John', 'age': 30, 'job': 'teacher'}
    person['city'] = 'Paris'
    print(person)

add_place(add_place)

# 4. Remove the 'age' key-value pair from person. Print the updated dictionary.
def no_age(person):
    person = {'name': 'John', 'age': 30, 'job': 'teacher', 'city': 'Paris'}
    del person['age']
    print(person)

no_age(no_age)

# 5. Iterate through the person dictionary and print out each key-value pair on a separate line.
def iterate_dict(person):
    person = {'name': 'John', 'job': 'teacher', 'city': 'Paris'}
    for key, value in person.items():
        print(f"Key: {key}, Value: {value}")

iterate_dict(iterate_dict)

# -----------------------------------------------------------------------------


# Importing sys for test function
import sys


# Custom Test Function
def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    msg = f"Test at line {linenum} {'PASSED' if did_pass else 'FAILED'}."
    print(msg)


# Function 1: count_vowels
def count_vowels(s: str) -> int:
    """
    Count the number of vowels in a string.

    Parameters:
    - s (str): The input string

    Returns:
    - int: The number of vowels in the string
    """
    vowel = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowel:
            count += 1
    return count


# Unit Tests for count_vowels
def test_count_vowels():
    test(count_vowels("hello") == 2)
    test(count_vowels("why") == 0)
    test(count_vowels("aeiou") == 5)
    test(count_vowels("") == 0)
    test(count_vowels("bcdfg") == 0)
    test(count_vowels("aeiouAEIOU") == 10)
    test(count_vowels("HELLO") == 2)
    test(count_vowels("aEiOu") == 5)
    test(count_vowels("a e i o u") == 5)
    test(count_vowels("rhythm") == 0)


# Function 2: merge_lists
def merge_lists(list1: list, list2: list) -> list:
    """
    Merge two sorted lists into a single sorted list.

    Parameters:
    - list1 (list): The first sorted list
    - list2 (list): The second sorted list

    Returns:
    - list: A new sorted list containing all elements from list1 and list2
    """
    import itertools
    merged = list(itertools.chain(list1, list2))
    n = len(merged)
    for i in range(n):
        for j in range(0, n-i-1):
            if merged[j] > merged[j+1]:
                merged[j], merged[j+1] = merged[j+1], merged[j]
    return merged


# Unit Tests for merge_lists
def test_merge_lists():
    list1 = [1, 3, 5]
    list2 = [2, 4, 6]
    merged = merge_lists(list1, list2)
    test(merged == [1, 2, 3, 4, 5, 6])
    test(merge_lists([], []) == [])
    test(merge_lists([1], [2]) == [1, 2])
    test(merge_lists([1, 1], [2, 2]) == [1, 1, 2, 2])
    test(merge_lists([1, 3, 5], []) == [1, 3, 5])
    test(merge_lists([], [2, 4, 6]) == [2, 4, 6])
    test(merge_lists([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6])
    test(merge_lists([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    test(merge_lists([1, 1, 2, 3], [1, 2, 2, 3]) == [1, 1, 1, 2, 2, 2, 3, 3])


# Function 3: word_lengths
def word_lengths(words: list) -> list:
    """
    Get the lengths of words in a list.

    Parameters:
    - words (list): The list of words

    Returns:
    - list: A list containing the lengths of the words
    """
    word_length = []
    for word in words:
        word_length.append(len(word))
    return word_length


# Unit Tests for word_lengths
def test_word_lengths():
    words = ["hello", "world", "python"]
    lengths = word_lengths(words)
    test(lengths == [5, 5, 6])
    test(word_lengths([]) == [])
    test(word_lengths(["word"]) == [4])
    test(word_lengths(["short", "mediummm", "longesttttt"]) == [5, 8, 11])
    test(word_lengths(["", "a", "ab", "abc"]) == [0, 1, 2, 3])
    test(word_lengths(["  ", "a b", " c "]) == [2, 3, 3])


# Function 4: reverse_string
def reverse_string(s: str) -> str:
    """
    Reverse a string.

    Parameters:
    - s (str): The input string

    Returns:
    - str: The reversed string
    """
    reversed_s = s[::-1]
    return reversed_s

# Unit Tests for reverse_string
def test_reverse_string():
    text = "python"
    reversed_text = reverse_string(text)
    test(reversed_text == "nohtyp")
    test(reverse_string("") == "")
    test(reverse_string("a") == "a")
    test(reverse_string("aaa") == "aaa")
    test(reverse_string("Hello, World!") == "!dlroW ,olleH")
    test(reverse_string("12345") == "54321")
    test(reverse_string("  spaces  ") == "  secaps  ")


# Function 5: intersection
def intersection(list1: list, list2: list) -> list:
    """
    Find the intersection of two lists.

    Parameters:
    - list1 (list): The first list
    - list2 (list): The second list

    Returns:
    - list: The intersection of the two lists
    """
    intersected_list = []
    size_of_list1 = len(list1)
    
    for itemct in range(size_of_list1):
        if list1[itemct] in list2:
            if list1[itemct] not in intersected_list:
                intersected_list.append(list1[itemct])
    return intersected_list


# Unit Tests for intersection
def test_intersection():
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    result = intersection(list1, list2)
    test(result == [3, 4])
    test(intersection([], []) == [])
    test(intersection([1, 2], [3, 4]) == [])
    test(intersection([1, 2], [1, 2]) == [1, 2])
    test(intersection([1, 2, 2, 3], [2, 2, 3, 4]) == [2, 3])
    test(intersection([1, 2, 3], [4, 5, 6]) == [])
    test(intersection([1, 2, 3], [1, 2, 3]) == [1, 2, 3])


# Test Suite
def test_suite():
    print(f"Count Vowels Test Results:")
    test_count_vowels()
    print(f"Merge Lists Test Results:")
    test_merge_lists()
    print(f"Word Lengths Test Results:")
    test_word_lengths()
    print(f"Reverse String Test Results:")
    test_reverse_string()
    print(f"Intersection Test Results:")
    test_intersection()


test_suite()
