"""Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized."""


def convert_to_camel_case(text):
    signs = {"_", "-", " "}
    for letter in text:
        if letter in signs:
            text = text.replace(letter, " ")

    FirstWord = text.find(" ")
    Word = text[:FirstWord]
    text = text[FirstWord:].title()
    text = text.split(" ")
    text = "".join(text)
    return Word + text


if __name__ == '__main__':

    assert convert_to_camel_case('') == ''
    assert convert_to_camel_case("the_stealth_warrior") == "theStealthWarrior"
    assert convert_to_camel_case("The-Stealth-Warrior") == "TheStealthWarrior"
    assert convert_to_camel_case("A-B-C") == "ABC"
