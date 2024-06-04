class SudokuSolver:

    def __init__(self):
        self.__sudoku = []
        self.__cur_row = 0
        self.__cur_col = 0

        with open('sudoku_example.txt') as file:
            content = file.read()
            rows = content.split('\n')

            for row in rows:
                cells = row.split(', ')
                try:
                    cells = [int(cell) for cell in cells]
                except ValueError:
                    raise ValueError('Sudoku board is not valid!') from None
                self.__sudoku.append(cells)

        if not self._is_board_valid():
            raise ValueError('Sudoku board is not valid!')

    def _save_result(self, ready_sudoku):
        with open('result.txt', 'a') as file:
            file.write(ready_sudoku)

    def _format_result(self):
        result = ''
        for row in self.__sudoku:
            for num in row:
                result += str(num) + ", "
            result = result[:-2] + "\n"
        return result

    def _is_board_valid(self):
        for row in self.__sudoku:
            if len(row) != 9:
                return False
            current_numbers = set()
            for num in row:
                if (num < 0 or num > 9 or num in current_numbers) and num != 0:
                    return False
                current_numbers.add(num)

        for col in range(9):
            current_numbers = set()
            for row in range(9):
                num = self.__sudoku[row][col]
                if (num < 0 or num > 9 or num in current_numbers) and num != 0:
                    return False
                current_numbers.add(num)

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                current_numbers = set()
                for b_row in range(i, i + 3):
                    for b_col in range(j, j + 3):
                        num = self.__sudoku[b_row][b_col]
                        if (num < 0 or num > 9 or num in current_numbers) and num != 0:
                            return False
                        current_numbers.add(num)

        return True

    def _is_num_possible(self, number, row, col):
        for i in range(9):
            if self.__sudoku[row][i] == number:
                return False

        for j in range(9):
            if self.__sudoku[j][col] == number:
                return False

        start_row = row - row % 3
        start_col = col - col % 3

        for i in range(3):
            for j in range(3):
                if self.__sudoku[start_row + i][start_col + j] == number:
                    return False

        return True

    def solve(self):
        row, col = None, None

        for r in range(self.__cur_row, 9):
            for c in range(self.__cur_col, 9):
                if self.__sudoku[r][c] == 0:
                    row, col = r, c
                    break
            break

        if row is None:
            result = self._format_result()
            self._save_result(result)
            return True

        for number in range(1, 10):
            if self._is_num_possible(number, row, col):
                self.__sudoku[row][col] = number
                if all(self.__sudoku[row]) != 0:
                    self.__cur_row, self.__cur_col = row + 1, 0
                else:
                    self.__cur_row, self.__cur_col = row, col + 1
                if self.solve():
                    return True
            self.__sudoku[row][col] = 0

        return False


sudoku = SudokuSolver()
sudoku.solve()
