"""Deadfish has 4 commands, each 1 character long:

"i" increments the value (initially 0)
"d" decrements the value
"s" squares the value
"o" outputs the value into the return array
Invalid characters should be ignored."""


def deadFish(data):

    answer = []
    accumulator = 0

    for letter in data:
        if letter == "o":
            answer.append(accumulator)
        elif letter == "i":
            accumulator += 1
        elif letter == "s":
            accumulator **= 2
        elif letter == "d":
            accumulator -= 1

    return answer


if __name__ == '__main__':


    assert deadFish("ooo") == [0, 0, 0]
    assert deadFish("ioioio") == [1, 2, 3]
    assert deadFish("idoiido") == [0, 1]
    assert deadFish("isoisoiso") == [1, 4, 25]
    assert deadFish("codewars") == [0]
