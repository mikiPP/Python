"""    
    Given a word of words, you need to find the highest scoring word.

Each letter of a word scores points according to it's position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a word.

All letters will be lowercase and all inputs will be valid."""


def highestScoringWord(sentence):
    LetterValue = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                   14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    Letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
               "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    dictionary = dict(zip(Letters, LetterValue))
    word = ""
    answer = ""
    count = 0
    max = 0

    for Letter in sentence:

        if Letter != " ":
            count += dictionary[Letter]
            word += Letter
            if count > max:
                max = count
                answer = word
                
        else:
            count = 0
            word = ""

    return answer

if __name__ == '__main__':


    assert highestScoringWord('man i need a taxi up to ubud') == "taxi"
    assert highestScoringWord('what time are we climbing up the volcano') == "volcano"
    assert highestScoringWord('take me to semynak') ==  "semynak"