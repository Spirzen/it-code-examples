from board import Board

def main() -> None:
    board = Board(8, 8, fill=1)
    print(board.get(0, 0), board.rows, board.cols)

if __name__ == "__main__":
    main()
