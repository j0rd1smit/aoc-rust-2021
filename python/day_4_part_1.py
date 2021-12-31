from typing import Dict, List, Tuple

import aocd
import numpy as np


def main():
    data = aocd.get_data(year=2021, day=4).split("\n")

    drawing_order = data[0].split(",")
    boards = []
    board_rows = []

    for row in data[2:]:
        if row == "":
            boards.append(Board.from_str_input(board_rows))
            board_rows = []
        else:
            board_rows.append(row.strip().split())
    boards.append(Board.from_str_input(board_rows))

    bingo = False
    bingo_board = None
    for i, v in enumerate(drawing_order):
        for j, board in enumerate(boards):
            board.mark(v)
            if board.is_solved:
                bingo_board = board
                bingo = True
                print(board.score(int(v)))

        if bingo:
            break


class Board:
    def __init__(
        self,
        item_to_location: Dict[str, Tuple[int, int]],
        marked_locations: np.ndarray,
        item_grid: np.ndarray,
    ):
        self._item_to_location = item_to_location
        self._marked_locations = marked_locations
        self.is_solved = self._check_if_is_solved()
        self.item_grid = item_grid

    @staticmethod
    def from_str_input(rows: List[List[str]]) -> "Board":
        item_to_location = {}
        marked_locations = np.zeros([len(rows), len(rows[0])], dtype=bool)
        item_grid = []
        for i, row in enumerate(rows):
            item_grid_row = []
            for j, v in enumerate(row):
                item_to_location[v] = i, j
                item_grid_row.append(int(v))
            item_grid.append(item_grid_row)

        return Board(item_to_location, marked_locations, np.array(item_grid))

    def mark(self, item: str) -> None:
        if item in self._item_to_location:
            x, y = self._item_to_location[item]
            self._marked_locations[x, y] = True
            self.is_solved = self._check_if_is_solved()

    def _check_if_is_solved(self) -> bool:
        n_rows, n_cols = self._marked_locations.shape
        return np.any(np.sum(self._marked_locations, axis=0) >= n_rows) or np.any(
            np.sum(self._marked_locations, axis=1) >= n_cols
        )

    def score(self, last_called):
        return last_called * np.sum(
            np.where(
                np.logical_not(self._marked_locations),
                self.item_grid,
                np.zeros_like(self.item_grid),
            )
        )


if __name__ == "__main__":
    main()
