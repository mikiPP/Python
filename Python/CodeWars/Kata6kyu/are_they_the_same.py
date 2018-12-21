"""Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure) 
that checks whether the two arrays have the "same" elements, with the same multiplicities. "Same" means, here, that the elements in b are the elements in a squared, regardless of the order."""


def comp(array1, array2):

    if array1 == None or array2 == None:
        return False

    for number in array1:
        if array1.count(number) != array2.count(number**2):
            return False

    return True


if __name__ == '__main__':

    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11 * 11, 121 * 121, 144 * 144, 19 * 19,
          161 * 161, 19 * 19, 144 * 144, 19 * 19]

    assert comp(a1, a2) == True
