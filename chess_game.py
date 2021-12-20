position_lookup={}
letter_list=['a','b','c','d','e','f','g','h']
row_count=1
                                                
for row in range(8):
    for col in range(8):
        position_lookup[f'{letter_list[col]}{row+1}']=[row,col]

class Invalid_move(Exception):
    pass
class Piece:
    def __init__(self,row,col,board,color) -> None:
        self.pos=[row,col]
        self.board=board
        self.color=color
        self.possible_moves=[]
        
        
class Pawn(Piece):
    def __init__(self,col,row,board,color):
        Piece.__init__(self,col,row,board,color)
        self.first_turn=True
        if self.color=='white':
            self.letter='P'
        else:
            self.letter='p'


    def move(self,board,piece,pos_input):
        self.last_move=board[piece.pos[0]][piece.pos[1]]
        self.get_possibel_moves(piece,board)
        if tuple(position_lookup[pos_input]) not in self.possible_moves:
            raise Invalid_move()
        board[piece.pos[0]][piece.pos[1]]='.'
        piece.pos=position_lookup[pos_input] 
        board[piece.pos[0]][piece.pos[1]]=piece

        return board
    def get_possible_moves(self,piece,board):
        self.start_pos=tuple(piece.pos)
        if self.first_turn:
            for i in range (2):
                piece.pos[0]+=1
                self.possible_moves.append(piece.pos)
        else:
            piece.pos+=1
            self.possible_moves.append(piece.pos)
    def make_move(self,piece,board,pos_input):
        try:
                board=self.move(board,piece,pos_input)
                return board
        except Invalid_move as err:
            print('caught invalid move',err)
            print('handle it???')
            return board
class Rook(Piece):
    def __init__(self,col,row,board,color) -> None:
        Piece.__init__(self,col,row,board,color)
        self.name='rook'
        if self.color=='white':
            self.letter='R'
        else:
            self.letter='r'

    def move(self,board,piece,pos_input):
        self.get_possible_moves(piece,board)
        print(f"{tuple(position_lookup[pos_input])} is the coord of the square you want to move to")
        if tuple(position_lookup[pos_input]) not in self.possible_moves:
            raise Invalid_move()
            
                
        self.last_move=board[piece.pos[0]][piece.pos[1]]
        print(piece.pos)
        board[piece.pos[0]][piece.pos[1]]='.'
        piece.pos=position_lookup[pos_input]
        
        board[piece.pos[0]][piece.pos[1]]=piece
        print(piece.pos)
        return board


    def get_possible_moves(self,piece,board):
        self.start_pos=tuple(piece.pos)
        
    
        up=True
        down=False
        left=False
        right=False
        
        while up:
            piece.pos[0]-=1
            self.possible_moves.append(tuple(piece.pos))
            
            if piece.pos[0]<=0:
                self.pos=[self.start_pos[0],self.start_pos[1]]
                up=False
                down=True
                
        while down:
            
            piece.pos[0]+=1
            self.possible_moves.append(tuple(piece.pos))
            
            if piece.pos[0]>=7:
                self.pos=[self.start_pos[0],self.start_pos[1]]
                down=False
                left=True
        while left:
            
            piece.pos[1]-=1
            self.possible_moves.append(tuple(piece.pos))
            
            if piece.pos[1]<=0:
                self.pos=[self.start_pos[0],self.start_pos[1]]
                left=False
                right=True
        while right:
            
            piece.pos[1]+=1
            self.possible_moves.append(tuple(piece.pos))
            
            if piece.pos[1]==7:
                self.pos=[self.start_pos[0],self.start_pos[1]]
                right=False
        
        self.pos=[self.start_pos[0],self.start_pos[1]]
        return board
    def make_move(self,board,piece,pos_input):
        try:
            board=self.move(board,piece,pos_input)
            return board
        except Invalid_move as err:
            print("Invalid",err)
            # Do something...
            raise err




class Bishop(Piece):
    def __init__(self,col,row,board,color) -> None:
        Piece.__init__(self,col,row,board,color)
        self.name='bishop'
        if self.color=='white':
            self.letter='B'
        else:
            self.letter='b'



    def move(self,board,piece,pos_input):
        self.last_move=board[piece.pos[0]][piece.pos[1]]
        self.get_possibel_moves(piece,board)
        if tuple(position_lookup[pos_input]) not in self.possible_moves:
            raise Invalid_move()
        board[piece.pos[0]][piece.pos[1]]='.'
        piece.pos=position_lookup[pos_input] 
        board[piece.pos[0]][piece.pos[1]]=piece

        return board
    def get_possibel_moves(self,piece,board) :
        self.start_pos=tuple(piece.pos)
        up=True
        down=False
        right=True
        left=False    

        while up and right:
            piece.pos[0]-=1
            piece.pos[1]-=1
            self.possible_moves.append(tuple(piece.pos))
            if piece.pos[0]<=0 or piece.pos[1]<=0:
                self.pos=[self.start_pos[0],self.start_pos[1]]
                right=False
                left=True
        while up and left:
            piece.pos[0]-=1
            piece.pos[1]+=1
            self.possible_moves.append(tuple(piece.pos))
            if self.pos[0]<=0 or self.pos[1]>=7:
                self.pos=[self.start_pos[0],self.start_pos[1]]
                down=True
                up=False

        while down and left:
            piece.pos[0]+=1
            piece.pos[1]+=1
            self.possible_moves.append(tuple(piece.pos))
            if piece.pos[0]>=7 or piece.pos[1]>=7:
                self.pos=[self.start_pos[0],self.start_pos[1]]
                left=False
                right=True
        while down and right:
            piece.pos[0]+=1
            piece.pos[1]-=1
            self.possible_moves.append(tuple(piece.pos))
            print (self.possible_moves)
            if piece.pos[0]>=7 or piece.pos[1]<=0:
                self.pos=[self.start_pos[0],self.start_pos[1]]
                down=False
                right=False
        return board
    def make_move(self,board,piece,pos_input):
        try:
            board=self.move(board,piece,pos_input)
            return board
        except Invalid_move as err:
            print('caught invalid move',err)
            print('handle it???')
            return board

class queen(Piece):
    def __init__(self):
        pass
class King(Piece): 
    def __init__(self,col,row,board,color) -> None:
        self.pos=[row,col]
        self.board=board
        self.color=color

class Board:
    def __init__ (self):
       
        self.board=[ ["."] * 8 for i in range(8)]
        self.x_change=False
        self.y_change=False
        self.direction=0
        self.test=False
        self.rw=Rook(4,4,self.board,'white')
        self.wb=Bishop(1,1,self.board,'black')
        self.wp=Pawn(3,3,self.board,'white')
        self.board[self.rw.pos[0]][self.rw.pos[1]]=self.rw
        self.board[self.wb.pos[0]][self.wb.pos[1]]=self.wb
        self.board[self.wp.pos[0]][self.wp.pos[1]]=self.wp

    def game_loop(self):
        running = True
        
        while running:
            
            user_input=input()
            if user_input.lower()=='play':
                
                self.make_moves()
            elif user_input.lower()=='reset display':
                self.display_update()

            if user_input.lower()=='stop':
                running=False

    def make_moves (self):
        user =input()
        self.make_moves_for_text(user)

    def make_moves_for_text (self, user):
        user.lower()
        
        user=user.split(' ')
        piece=user[0]
        
        pos_input=user[3]
        pos=self.rw.pos
        print(user)
        if piece=='rook':
            print('rook')
            piece=self.rw
           
            
            self.board=piece.make_move(self.board,piece,pos_input)
            
            
            if piece.pos[0]<0:
                print('error')
            elif piece.pos[1]<0:
                print('error')
                
            else:
                self.display_update()
        if piece=='bishop':
            piece=self.wb
            
            self.board=self.wb.make_move(self.board,piece,pos_input)
            if not self.board:
                raise Exception('WHHHHHHAAAAAAAA')

            if self.wb.pos[0]<0:
                print('error')
            elif self.wb.pos[1]<0:
                print('error')
            else:
                self.display_update()
        if piece=='pawn':
            piece=self.wp
           
            
            self.board=piece.make_move(self.board,piece,pos_input)

    def display_update(self):
        #play
        # print(self.board)
      
        print("  A B C D E F G H")
        for rn,row in enumerate(self.board):
            print(rn+1,end='')
            
            for square in row:
                print('|',end='')
                if isinstance(square,Piece):
                    
                    print (square.letter,end='')
                    
                else:
                    
                    print(square,end='')
            
            print('')
    def check_for_take(self):
        pass


def test_rook():
    bored=Board()
    bored.display_update()

def test_get_moves():
    board=Board()
    piece=board.board[4][4]
    piece.get_possible_moves(board.rw,board.board)
    print(piece.possible_moves)
def test_make_moves():
    board=Board()


def test_text_ui ():
    board = Board()
    board.make_moves_for_text('pawn b2 to d4')
    #board.make_moves_for_text('bishop c3 to b2')
    #board.make_moves_for_text('bishop d2 to e8')


test_text_ui()


#test_get_moves()
#bored=Board()
#bored.display_update()
#sbored.game_loop()