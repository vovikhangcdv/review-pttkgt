#!/usr/bin/env python3
"""The n queens puzzle."""


class NQueens:
    """Generate all valid solutions for the n queens puzzle"""

    def __init__(self, size):
        # Store the puzzle (problem) size and the number of valid solutions
        self.size = size
        self.solutions = 0
        self.step = 0
        self.quit = False
        self.solve()

    def solve(self):
        """Solve the n queens puzzle and print the number of solutions"""
        positions = [-1] * self.size
        self.put_queen(positions, 0)
        print("Found", self.solutions, "solutions.")

    def put_queen(self, positions, target_row):
        """
        Try to place a queen on target_row by checking all N possible cases.
        If a valid place is found the function calls itself trying to place a queen
        on the next row until all N queens are placed on the NxN board.
        """
        # Base (stop) case - all N rows are occupied
        if self.quit:
            return
        if target_row == self.size:
            self.solutions += 1
            print("This is also the solution {}!".format(self.solutions))
            Respond = input("Continue (Y/N)? ").strip().upper()
            if Respond != 'Y':
                self.quit = True
                return
        else:
            # For all N columns positions try to place a queen
            for column in range(self.size):
                # Reject all invalid positions
                if self.check_place(positions, target_row, column):
                    if self.quit:
                        return
                    positions[target_row] = column
                    self.step += 1
                    print("Step {}:".format(self.step))
                    self.show_full_board(positions)
                    self.put_queen(positions, target_row + 1)
                    positions[target_row] = -1

    def check_place(self, positions, ocuppied_rows, column):
        """
        Check if a given position is under attack from any of
        the previously placed queens (check column and diagonal positions)
        """
        for i in range(ocuppied_rows):
            if positions[i] == column or positions[i] - i == column - ocuppied_rows or positions[i] + i == column + ocuppied_rows:

                return False
        return True

    def show_full_board(self, positions):
        """Show the full NxN board"""
        for row in range(self.size):
            line = ""
            for column in range(self.size):
                if positions[row] == column:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print()


def nQueensPuzzle():
    """Initialize and solve the n queens puzzle"""
    n = input("Number of queens?: ")
    NQueens(int(n))


if __name__ == "__main__":
    # execute only if run as a script
    nQueensPuzzle()
