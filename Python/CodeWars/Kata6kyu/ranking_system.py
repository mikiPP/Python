"""
ou are given an array of unique numbers. The numbers represent points. The higher the number the higher the points.
In the array [1,3,2] 3 is the highest point value so it gets 1st place. 2 is the second highest so it gets second place. 1 is the 3rd highest so it gets 3rd place.

Your task is to return an array giving each number its rank in the array.

input // [1,3,2] 
output // [3,1,2]
rankings([1,2,3,4,5]) // [5,4,3,2,1] 
rankings([3,4,1,2,5])// [3,2,5,4,1] 
rankings([10,20,40,50,30]) // [5, 4, 2, 1, 3] 
"""


def rankings(arr):
    answer = arr[:]
    auxiliar = arr[:]
    auxiliar.sort()
    auxiliar.reverse()
    for number in arr:
        position = arr.index(number)
        answer[position] = auxiliar.index(number) + 1
    return answer


if __name__ == '__main__':

    assert rankings([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert rankings([3, 4, 1, 2, 5]) == [3, 2, 5, 4, 1]
    assert rankings([10, 20, 40, 50, 30]) == [5, 4, 2, 1, 3]
