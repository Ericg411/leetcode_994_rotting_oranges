import unittest
from solution import Solution

class TestRottingOranges(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_fresh_orange(self):
        grid = [[1]]
        self.assertEqual(self.solution.orangesRotting(grid), -1)

    def test_single_rotten_orange(self):
        grid = [[2]]
        self.assertEqual(self.solution.orangesRotting(grid), 0)

    def test_no_oranges(self):
        grid = [[0]]
        self.assertEqual(self.solution.orangesRotting(grid), 0)

    def test_mixed_oranges(self):
        grid = [
            [2, 1, 1],
            [1, 1, 0],
            [0, 1, 1]
        ]
        self.assertEqual(self.solution.orangesRotting(grid), 4)

    def test_isolated_fresh_oranges(self):
        grid = [
            [2, 0, 1],
            [0, 1, 0],
            [1, 0, 2]
        ]
        self.assertEqual(self.solution.orangesRotting(grid), -1)

    def test_all_rotten_oranges(self):
        grid = [
            [2, 2, 2],
            [2, 2, 2],
            [2, 2, 2]
        ]
        self.assertEqual(self.solution.orangesRotting(grid), 0)

    def test_all_fresh_oranges(self):
        grid = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        self.assertEqual(self.solution.orangesRotting(grid), -1)

    def test_no_rotten_oranges(self):
        grid = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
        self.assertEqual(self.solution.orangesRotting(grid), -1)

if __name__ == "__main__":
    unittest.main()