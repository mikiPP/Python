"""
Find the first character that repeats in a String and return that character.

first_dup('tweet') => 't'
first_dup('like') => None
This is not the same as finding the character that repeats first. In that case, an input of 'tweet' would yield 'e'.

"""


def first_duplicated(string):
    for letter in string:
        if string.count(letter) > 1:
            return letter
    return None


if __name__ == '__main__':

    assert first_duplicated('tweet') == 't'
    assert first_duplicated('Ode to Joy') == ' '
    assert first_duplicated('ode to joy') == 'o'
    assert first_duplicated('bar') == None
    assert first_duplicated('123123') == '1'
    assert first_duplicated('!@#$!@#$') == '!'
    assert first_duplicated('1a2b3a3c') == 'a'
