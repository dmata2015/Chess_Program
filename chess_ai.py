from multiprocessing.sharedctypes import Value
import chess




point_value={
    'p':1,
    'n':3,
    'b':3,
    'r':5,
    'q':9,
    'P':1,
    'N':3,
    'B':3,
    'R':5,
    'Q':9
}
white_lst=['P','N','B','R','Q']
black_lst=['p','n','b','r','q']
def eval(board):
    multiplier=1
    value=0
    board_value=0
    fen=board.fen()
    info_lst=str(fen).split(' ')
    row_list=str(info_lst[0]).split('/')
    for row in row_list:
        for square in row:
            if square in white_lst:
                multiplier=1
                value=point_value[square]*multiplier
            elif square in black_lst:
                multiplier=-1
                value=point_value[square]*multiplier
            else:
                value=0
            board_value+=value

    return board_value
def engine(depth,board):
    possible_moves=list(board.legal_moves)
    counter=0
    print(list(possible_moves))
    for level in range(depth):
        for move in possible_moves:
            
            cboard=board.copy()
            print(str(move))
            print(board)
            counter+=1
            cboard.push(move)
            print(board)
            print(eval(cboard))
            possible_moves.remove(move)
            cboard.pop()
    

    print(counter)

def test_eval():
    board=chess.Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
    print(eval(board))
def test_engine():
    board=chess.Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
    engine(3,board)

test_engine()
#test_eval()