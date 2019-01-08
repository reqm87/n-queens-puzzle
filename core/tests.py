from tests_data import ncases
from queens_puzzle import QueensPuzzle

class Tests_QueensPuzzle(object):

    def test_ncase_1(self):
        assert QueensPuzzle(ncases[0]["n"]).solutions == ncases[0]["solutions"]

    def test_ncase_2(self):
        assert QueensPuzzle(ncases[1]["n"]).solutions == ncases[1]["solutions"]

    def test_ncase_3(self):
        assert QueensPuzzle(ncases[2]["n"]).solutions == ncases[2]["solutions"]

    def test_ncase_4(self):
        assert QueensPuzzle(ncases[3]["n"]).solutions == ncases[3]["solutions"]

    def test_ncase_5(self):
        assert QueensPuzzle(ncases[4]["n"]).solutions == ncases[4]["solutions"]

    def test_ncase_6(self):
        assert QueensPuzzle(ncases[5]["n"]).solutions == ncases[5]["solutions"]

    def test_ncase_7(self):
        assert QueensPuzzle(ncases[6]["n"]).solutions == ncases[6]["solutions"]

    def test_ncase_8(self):
        assert QueensPuzzle(ncases[7]["n"]).solutions == ncases[7]["solutions"]

    def test_ncase_9(self):
        assert QueensPuzzle(ncases[8]["n"]).solutions == ncases[8]["solutions"]

    def test_ncase_10(self):
        assert QueensPuzzle(ncases[9]["n"]).solutions == ncases[9]["solutions"]

    def test_ncase_11(self):
        assert QueensPuzzle(ncases[10]["n"]).solutions == ncases[10]["solutions"]

    def test_ncase_12(self):
        assert QueensPuzzle(ncases[11]["n"]).solutions == ncases[11]["solutions"]

