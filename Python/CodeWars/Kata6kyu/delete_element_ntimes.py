"""Given a list lst and a number N, create a new list that contains each number of lst at most N times without reordering.
Given a list lst and a number N, create a new list that contains each number of lst at most N times without reordering.
20,37,20,21}, 1) // return [20,37,21]"""


def delete_number_ntimes(order, n):

    for element in order:
        while order.count(element) > n:
            order.reverse()
            order.remove(element)
            order.reverse()
    return order


if __name__ == '__main__':
    assert delete_number_ntimes([20, 37, 20, 21], 1) == [20, 37, 21]
    assert delete_number_ntimes([1, 1, 3, 3, 7, 2, 2, 2, 2], 3) == [
        1, 1, 3, 3, 7, 2, 2, 2]
