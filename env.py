class IllegalMove(Exception):
    pass


class Connect4:
    def __init__(self):
        self.player = 1
        self.grid = [[0 for _ in range(10)] for __ in range(10)]

    def play(self, position: int) -> int:
        if position >= len(self.grid):
            raise IllegalMove
        for i, cell in enumerate(self.grid[position]):
            if cell == 0:
                self.grid[position][i] = self.player
                break
        else:
            raise IllegalMove(f"Column {position} is full")
        self.player = 1 if self.player == 2 else 2
        return self.detect_winner()

    def detect_winner(self) -> int:
        for func in (
            self._detect_line_in_col,
            self._detect_line_in_col,
            self._detect_line_in_diagonal_right,
            self._detect_line_in_diagonal_left,
        ):
            if winner := func():
                return winner
        return 0

    def _detect_line_in_col(self) -> int:
        for col in self.grid:
            count = 1
            previous, *col = col
            for cell in col:
                if cell == 0:
                    break
                elif cell == previous:
                    count += 1
                    if count == 4:
                        return cell
                else:
                    previous = cell
                    count = 0
        return 0

    def _detect_line_in_row(self) -> int:
        for row_index in range(len(self.grid[0])):
            count = 0
            previous = self.grid[0][0]
            for col_index in range(len(self.grid)):
                cell = self.grid[col_index][row_index]
                if cell != previous:
                    count = 0
                if cell == 0:
                    continue
                count += 1
                if count == 4:
                    return cell
                previous = cell
        return 0

    def _detect_line_in_diagonal_right(self) -> int:
        for diagonal_index in range(7):
            count = 1
            previous = self.grid[diagonal_index][0]
            for i in range(1, len(self.grid)):
                if i + diagonal_index >= len(self.grid):
                    continue
                cell = self.grid[i + diagonal_index][i]
                if cell == 0:
                    count = 0
                    continue
                if cell != previous:
                    count = 0
                count += 1
                if count == 4:
                    return cell
                previous = cell
        return 0

    def _detect_line_in_diagonal_left(self) -> int:
        for diagonal_index in range(3, len(self.grid)):
            count = 1
            previous = self.grid[diagonal_index][0]
            for i in range(len(self.grid)):
                if diagonal_index - i < 0:
                    continue
                cell = self.grid[diagonal_index - i][i]
                if cell == 0:
                    count = 0
                    continue
                if cell != previous:
                    count = 0
                count += 1
                if count == 4:
                    return cell
                previous = cell
        return 0

    def __str__(self):
        rows = []
        for row_index in range(len(self.grid[0]) - 1, -1, -1):
            row = []
            for col_index in range(len(self.grid)):
                row.append(str(self.grid[col_index][row_index]))
            rows.append("  ".join(row))
        return "\n".join(rows)


if __name__ == "__main__":
    game = Connect4()
    game.play(0)
    game.play(0)
    print(game)
