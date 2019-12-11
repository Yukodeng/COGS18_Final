import functions as f


def test_Board():
    board = f.Board(rows=5, ballcount=40, height=20)
    assert board.x == 5
    assert len(board.stack) == 6
    assert len(board.grid_list) == 30
    assert type(board.on_display()) == bool



test_Board()