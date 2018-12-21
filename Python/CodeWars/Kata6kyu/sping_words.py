"""Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata).
 Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present."""


def spin_words(sentence):
    sentence += " "
    string = ""
    count = 0
    answer = ""
    for letter in sentence:

        if count == len(sentence):
            if count > 5:

                string = list(string)
                string.reverse()
                strin = "".join(string)
                return sentence.strip()

            else:
                return sentence.strip()

        elif letter == " ":
            if count >= 5:
                string = list(string)
                string.reverse()
                string = "".join(string)
                answer += string + " "
            else:
                answer += string + " "

            string = ""
            count = 0
        else:
            count += 1
            string += letter

    return answer.strip()


if __name__ == '__main__':

    assert "emocleW" == spin_words("Welcome")
    assert "Hey wollef sroirraw" == spin_words("Hey fellow warriors")
