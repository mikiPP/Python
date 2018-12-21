"""Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that 
occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits."""


def duplicate_count(text):
    text = text.lower()
    letrasRepetidas = []

    for letra in text:
        if text.count(letra) > 1 and letra not in letrasRepetidas:
            letrasRepetidas.append(letra)

    return len(letrasRepetidas)


if __name__ == '__main__':

    assert duplicate_count("abcde") == 0
    assert duplicate_count("abcdea") == 1
    assert duplicate_count("indivisibility") == 1
