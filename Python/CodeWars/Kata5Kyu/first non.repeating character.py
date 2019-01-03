"""
Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.
"""


def first_non_repeating_letter(string):

    string2 = string.lower()
    letterFound = False
    letterPosition = 0

    for letter in string2:
        if string2.count(letter) == 1 and letterFound == False:
            letterPosition = string2.find(letter)
            letterFound = True

    if letterFound:
        return string[letterPosition]

    return ""


if __name__ == '__main__':
    assert first_non_repeating_letter('a') == 'a'
    assert first_non_repeating_letter('stress') == 't'
    assert first_non_repeating_letter('moonmen') == 'e'
