"""Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number.
 You can guarantee that input is non-negative."""


def countBits(decimal):
    i = 0
    j = 0
    string = bin(decimal)
    while j < len(string):
        if string[j] == "1":
            i = i + 1
        j = j + 1

    return i


if __name__ == '__main__':
    assert countBits(0) == 0
    assert countBits(4) == 1
    assert countBits(7) == 3
    assert countBits(9) == 2
    assert countBits(10) == 2
