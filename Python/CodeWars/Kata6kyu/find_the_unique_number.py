"""There is an array with some numbers. All numbers are equal except for one. Try to find it!
The tests contain some very huge arrays, so think about performance."""


def find_unique_number(array):
    return max(array) if array.count(max(array)) == 1 else min(array)


if __name__ == '__main__':
    assert find_unique_number([1, 1, 1, 2, 1, 1]) == 2
    assert find_unique_number([0, 0, 0.55, 0, 0]) == 0.55
    assert find_unique_number([3, 10, 3, 3, 3]) == 10
