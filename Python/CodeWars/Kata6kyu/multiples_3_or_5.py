# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
def Get_Multiples_3_or_5(number):
    countMultiples = 0
    number = number - 1
    while number >= 0:
        if number % 3 == 0 or number % 5 == 0:
            countMultiples = countMultiples + number
        number = number - 1
    return countMultiples


if __name__ == '__main__':
    assert Get_Multiples_3_or_5(10) == 23
