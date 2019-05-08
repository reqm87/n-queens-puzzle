from queens_puzzle import QueensPuzzle
from tests_data import ncases


class TestQueensPuzzle(object):
    def test_ncases(self):
        for i in range(1, 13):
            assert QueensPuzzle(i).solutions == ncases[i - 1]["solutions"]
