def is_prime(number):
    position = 2
    while position < number:
        if number % position == 0:
            return False
        position = position + 1
    if position == number:
        return True
    else:
        return False


if __name__ == '__main__':
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(2) == True
