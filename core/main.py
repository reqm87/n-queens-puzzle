from queens_puzzle import QueensPuzzle
from orm.database import db_access

def main():
    for n in range(8, 15):
        QueensPuzzle(n)


if __name__ == "__main__":
    main()

