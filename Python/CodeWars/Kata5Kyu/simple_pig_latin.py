# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.


def pig_it(text):
    space = False
    answer = ""
    pos = 1
    letter = text[0]

    while pos < len(text):

        if text[pos] != " " and space == False:
            answer += text[pos]

        elif text[pos] == " ":
            space = True
            answer += letter
            answer += text[pos]

        elif space == True:
            letter = text[pos]
            space = False

        pos += 1

    answer += letter
    answer = answer.split(" ")

    if "!" in answer or "?" in answer:
        return "ay ".join(answer)
    else:
        answer.append(" ")
        answer = "ay ".join(answer)
        return answer.strip()


if __name__ == '__main__':
    assert pig_it('Pig latin is cool') == 'igPay atinlay siay oolcay'
    assert pig_it('This is my string') == 'hisTay siay ymay tringsay'
