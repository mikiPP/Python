class Sudoku:

    """Sudoku Solution Validator"""

    def validSolution(sudoku):
        if Sudoku.checkNumbers(sudoku) == True and Sudoku.checkRows(sudoku) == True and Sudoku.checkColumn(sudoku) == True and Sudoku.checkBoxes(sudoku) == True:
            return True
        else:
            return False

    def checkNumbers(sudoku):
        for fila in sudoku:
            for numero in fila:
                if numero not in range(1, len(sudoku) + 1):
                    return False
        return True

    def checkRows(sudoku):

        for fila in sudoku:
            for numero in fila:
                if fila.count(numero) != 1:
                    return False
        return True

    def checkColumn(sudoku):

        posColumna = 0

        while posColumna < len(sudoku[0]):
            posFila = 0
            while posFila < len(sudoku):
                posFilab = posFila + 1
                while posFilab < len(sudoku):
                    if sudoku[posFila][posColumna] == sudoku[posFilab][posColumna]:
                        return False
                    posFilab += 1
                posFila += 1
            posColumna += 1

        return True

    def checkBoxes(sudoku):
        correcto = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for fila in range(3):
            for columna in range(3):
                region = []
                for line in sudoku[fila * 3:(fila + 1) * 3]:
                    region += line[columna * 3:(columna + 1) * 3]

                if sorted(region) != correcto:
                    return False

        return True


if __name__ == '__main__':

    sudoku1 = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
               [6, 7, 2, 1, 9, 5, 3, 4, 8],
               [1, 9, 8, 3, 4, 2, 5, 6, 7],
               [8, 5, 9, 7, 6, 1, 4, 2, 3],
               [4, 2, 6, 8, 5, 3, 7, 9, 1],
               [7, 1, 3, 9, 2, 4, 8, 5, 6],
               [9, 6, 1, 5, 3, 7, 2, 8, 4],
               [2, 8, 7, 4, 1, 9, 6, 3, 5],
               [3, 4, 5, 2, 8, 6, 1, 7, 9]]

    assert Sudoku.validSolution(sudoku1) == True

    sudoku2 = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
               [6, 7, 2, 1, 9, 0, 3, 4, 9],
               [1, 0, 0, 3, 4, 2, 5, 6, 0],
               [8, 5, 9, 7, 6, 1, 0, 2, 0],
               [4, 2, 6, 8, 5, 3, 7, 9, 1],
               [7, 1, 3, 9, 2, 4, 8, 5, 6],
               [9, 0, 1, 5, 3, 7, 2, 1, 4],
               [2, 8, 7, 4, 1, 9, 6, 3, 5],
               [3, 0, 0, 4, 8, 1, 1, 7, 9]]

    assert Sudoku.validSolution(sudoku2) == False

    sudoku3 = [[1, 3, 2, 5, 7, 9, 4, 6, 8],
               [4, 9, 8, 2, 6, 1, 3, 7, 5],
               [7, 5, 6, 3, 8, 4, 2, 1, 9],
               [6, 4, 3, 1, 5, 8, 7, 9, 2],
               [5, 2, 1, 7, 9, 3, 8, 4, 6],
               [9, 8, 7, 4, 2, 6, 5, 3, 1],
               [2, 1, 4, 9, 3, 5, 6, 8, 7],
               [3, 6, 5, 8, 1, 7, 9, 2, 4],
               [8, 7, 9, 6, 4, 2, 1, 5, 3]]

    assert Sudoku.validSolution(sudoku3) == True

    sudoku4 = [[1, 3, 2, 5, 7, 9, 4, 6, 8],
               [4, 9, 8, 2, 6, 1, 3, 7, 5],
               [7, 5, 6, 3, 8, 4, 2, 1, 9],
               [6, 4, 3, 1, 5, 8, 7, 9, 2],
               [5, 2, 1, 7, 9, 3, 8, 4, 6],
               [9, 8, 7, 4, 2, 6, 5, 3, 1],
               [2, 1, 4, 9, 3, 5, 6, 8, 7],
               [3, 6, 5, 8, 1, 7, 9, 2, 4],
               [8, 7, 9, 6, 4, 2, 1, 3, 5]]

    assert Sudoku.validSolution(sudoku4) == False

    sudoku5 = [[1, 3, 2, 5, 7, 9, 4, 6, 8],
               [4, 9, 8, 2, 6, 0, 3, 7, 5],
               [7, 0, 6, 3, 8, 0, 2, 1, 9],
               [6, 4, 3, 1, 5, 0, 7, 9, 2],
               [5, 2, 1, 7, 9, 0, 8, 4, 6],
               [9, 8, 0, 4, 2, 6, 5, 3, 1],
               [2, 1, 4, 9, 3, 5, 6, 8, 7],
               [3, 6, 0, 8, 1, 7, 9, 2, 4],
               [8, 7, 0, 6, 4, 2, 1, 3, 5]]

    assert Sudoku.validSolution(sudoku5) == False

    sudoku6 = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
               [2, 3, 4, 5, 6, 7, 8, 9, 1],
               [3, 4, 5, 6, 7, 8, 9, 1, 2],
               [4, 5, 6, 7, 8, 9, 1, 2, 3],
               [5, 6, 7, 8, 9, 1, 2, 3, 4],
               [6, 7, 8, 9, 1, 2, 3, 4, 5],
               [7, 8, 9, 1, 2, 3, 4, 5, 6],
               [8, 9, 1, 2, 3, 4, 5, 6, 7],
               [9, 1, 2, 3, 4, 5, 6, 7, 8]]

    assert Sudoku.validSolution(sudoku6) == False
