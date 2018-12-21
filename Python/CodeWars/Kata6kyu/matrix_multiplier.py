# this program calculates the matrix a * matrix b
def getMatrixProduct(matrixA, matrixB):

    if len(matrixA[0]) != len(matrixB):
        return - 1

    positionRowA = 0
    result = []
    rowResult = []

    while positionRowA < len(matrixA):

        positionColB = 0

        while positionColB < len(matrixB[0]):

            multiplicationResult = 0
            currentIndex = 0

            while currentIndex < len(matrixA[0]):
                multiplicationResult += matrixA[positionRowA][currentIndex] * \
                    matrixB[currentIndex][positionColB]
                currentIndex += 1

            rowResult.append(multiplicationResult)
            positionColB += 1

        result.append(rowResult)
        rowResult = []
        positionRowA += 1

    return result


if __name__ == '__main__':
        # Handles multiplication of 1x1 matrices
    assert getMatrixProduct([[2]], [[3]]) == [[6]]

    # Handles multiplication of 2x2 matrices
    assert getMatrixProduct([[1, 2], [3, 4]], [[5, 6], [7, 8]]) == [
        [19, 22], [43, 50]]

    # Handles multiplication of matrices including decimals
    assert getMatrixProduct([[0.5, 1], [1.5, 2]], [[0.2, 0.4], [0.6, 0.8]]) == [
        [0.7, 1.0], [1.5, 2.2]]

    # Returns -1 if matrices cannot be multiplied
    assert getMatrixProduct([[1, 2], [3, 4]], [[2, 4]]) == -1
