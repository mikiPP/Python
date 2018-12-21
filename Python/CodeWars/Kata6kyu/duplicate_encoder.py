def duplicateEncoder(string):
    string = string.lower()
    answer = ""
    for letter in string:

        if string.count(letter) == 1:
            answer += "("

        else:
            answer += ")"

    return answer


# Another Solutuion
"""def duplicateEncoder(string):
	string = string.lower()
	answer = ""
	letters = {}

	for letter in string:
		if letter in letters:
			 letters[letter] = ')'
        else:
            letters[letter] = '('

    for letter in string:
    	answer += letters[letter]"""


if __name__ == '__main__':

    Noserepite = "din"

    assert duplicateEncoder(Noserepite) == "((("

    Serepite = "aaaa"

    assert duplicateEncoder(Serepite) == "))))"

    caso1 = "recede"

    assert duplicateEncoder(caso1) == "()()()"

    caso2 = "Success"

    assert duplicateEncoder(caso2) == ")())())"
