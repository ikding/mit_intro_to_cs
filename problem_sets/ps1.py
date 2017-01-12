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
    ord_list = [ord(s[0])]
    longest_ord_list = []
    for char in s[1:]:
        if ord(char) >= ord_list[-1]:
            ord_list.append(ord(char))
            if len(ord_list) > len(longest_ord_list):
                longest_ord_list = ord_list
        else:
            if len(ord_list) > len(longest_ord_list):
                longest_ord_list = ord_list
            ord_list = [ord(char)]

    # print(longest_ord_list)
    if longest_ord_list:
        longest_chr = ''.join([chr(n) for n in longest_ord_list])
    else:
        longest_chr = ''

    return longest_chr
    # return 'Longest substring in alphabetical order is: {}'.format(longest_chr)


def test_count_longest_alphabetical_1():
    assert count_longest_alphabetical('abcbcd') == 'abc'
    assert count_longest_alphabetical('azcbobobegghakl') == 'beggh'


def test_count_longest_alphabetical_2():
    assert count_longest_alphabetical('qlonbwshkxfpwe') == 'hkx'
    assert count_longest_alphabetical('ldiyhcuru') == 'diy'
    assert count_longest_alphabetical('phfcxghvvqayqtjizfykrezi') == 'ghvv'
    assert count_longest_alphabetical('dlheaxgtubkjdsmucbpefpg') == 'gtu'
    assert count_longest_alphabetical('fcdpesqxjhvitnqp') == 'cdp'
    assert count_longest_alphabetical('atepyeuurgwpnqn') == 'epy'
    assert count_longest_alphabetical('ygdsrfroniqrfes') == 'iqr'
    assert count_longest_alphabetical('abcdefghijklmnopqrstuvwxyz') == 'abcdefghijklmnopqrstuvwxyz'
    assert count_longest_alphabetical('rujjycqyhmbg') == 'jjy'
    assert count_longest_alphabetical('llhwdwmw') == 'll'
    assert count_longest_alphabetical('dktvaevhejohjkimmvzeycb') == 'immvz'
    assert count_longest_alphabetical('zyxwvutsrqponmlkjihgfedcba') == 'z'
    assert count_longest_alphabetical('ryqqvzqljie') == 'qqvz'
    assert count_longest_alphabetical('efyprfogiigs') == 'efy'
    assert count_longest_alphabetical('cmsvucohvqaxpoytnvdek') == 'cmsv'
    assert count_longest_alphabetical('cdlmffrzkdlgmposcxvxmm') == 'cdlm'
    assert count_longest_alphabetical('bacjjrhbcozkftxblxn') == 'acjjr'
    assert count_longest_alphabetical('zjqifvgxlmmcrpwmnebgsnu') == 'lmm'
    assert count_longest_alphabetical('kolpmbhxmfnxvvncve') == 'bhx'
    assert count_longest_alphabetical('xsytjnun') == 'jnu'
