"""Problem Set 1"""


def count_vowel(s):
    """
    Assume s is a string of lower case characters. Write a program that counts
    up the number of vowels contained in the strings. Valid vowels are:
    'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl',
    your program should print:

    Number of vowels: 5
    """
    count = 0
    for char in s:
        if char in ['a', 'e', 'i', 'o', 'u']:
            count += 1

    return 'Number of vowels: {}'.format(count)


def test_count_vowel():
    assert count_vowel('dqbuytgooix') == 'Number of vowels: 4'


def count_bob(s):
    """
    Assume s is a string of lower case characters.

    Write a program that prints the number of times the string 'bob' occurs
    in s. For example, if s = 'azcbobobegghakl', then your program should
    print:

    Number of times bob occurs is: 2
    """
    count = 0
    for i in range(len(s) - 3):
        if s[i : i+3] == 'bob':
            count += 1

    output = 'Number of times bob occurs is: {}'.format(count)
    return output


def count_longest_alphabetical(s):
    """
    Assume s is a string of lower case characters.

    Write a program that prints the longest substring of s in which the letters
    occur in alphabetical order. For example, if s = 'azcbobobegghakl', then
    your program should print:

        Longest substring in alphabetical order is: beggh

    In the case of ties, print the first substring. For example,
    if s = 'abcbcd', then your program should print:

        Longest substring in alphabetical order is: abc

    Note: This problem may be challenging. We encourage you to work smart.
    If you've spent more than a few hours on this problem, we suggest that you
    move on to a different part of the course. If you have time, come back to
    this problem after you've had a break and cleared your head.
    """
