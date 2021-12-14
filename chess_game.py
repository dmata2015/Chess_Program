position_lookup={}
letter_list=['a','b','c','d','e','f','g','h']
row_count=1
                                                
for row in range(8):
    for col in range(8):
        position_lookup[f'{letter_list[col]}{row+1}']=[row,col]


class Piece:
    def __init__(self,row,col,board,color) -> None:
        self.pos=[row,col]
        self.board=board
        self.color=color
        self.possible_moves=[]
class Rook(Piece):
    def __init__(self,col,row,board,color) -> None:
        Piece.__init__(self,col,row,board,color)
        self.name='rook'
        self.letter='R'

    def move(self,board,piece,pos_input):
        self.last_move=board[piece.pos[0]][piece.pos[1]]
        board[piece.pos[0]][piece.pos[1]]='.'
        piece.pos=position_lookup[pos_input] 
        board[piece.pos[0]][piece.pos[1]]=piece
        return board


    def get_possible_moves(self,y_change,user,direction,piece,board):
        if y_change:
            
            board[piece.pos[0]][piece.pos[1]]="."
            board[piece.pos[0] - (direction * int(user[2]))][piece.pos[1]]=piece
            piece.pos=[(piece.pos[0] - (direction * int(user[2]))),piece.pos[1]]
        else:
            
            board[piece.pos[0]][piece.pos[1]]="."
            board[piece.pos[0]][piece.pos[1] - (direction * int(user[2]))]=piece
            piece.pos=[piece.pos[0],(piece.pos[1] - (direction * int(user[2])))]
            board=self.board
        return board
class Bishop(Piece):
    def __init__(self,col,row,board,color) -> None:
        Piece.__init__(self,col,row,board,color)
        self.name='bishop'
        self.letter='B'
    def move(self,board,piece,pos_input):
        self.last_move=board[piece.pos[0]][piece.pos[1]]
        board[piece.pos[0]][piece.pos[1]]='.'
        piece.pos=position_lookup[pos_input] 
        board[piece.pos[0]][piece.pos[1]]=piece
        return board
    def get_possibel_moves(self,y_negative_change,x_negative_change,user,piece,board) :
        if y_negative_change and x_negative_change:
            print('down left')
            board[piece.pos[0]][piece.pos[1]]='.'
            board[piece.pos[0]+int(user[3])][piece.pos[1]-int(user[3])]=piece

            

        elif y_negative_change and not x_negative_change:
            print('down right')
            board[piece.pos[0]][piece.pos[1]]='.'
            board[piece.pos[0]+int(user[3])][piece.pos[1]+int(user[3])]=piece
            y_negative_change=False
            x_negative_change=False
            
        elif not y_negative_change and x_negative_change:
            print('up left')
            board[piece.pos[0]][piece.pos[1]]='.'
            board[piece.pos[0]-int(user[3])][piece.pos[1]-int(user[3])]=piece
            y_negative_change=False
            x_negative_change=False

        elif not y_negative_change and not x_negative_change:
            print('up right')
            board[piece.pos[0]][piece.pos[1]]='.'
            board[piece.pos[0]-int(user[3])][piece.pos[1]+int(user[3])]=piece
            
            
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
        #print(self)
        self.direction=0
        self.test=False
        self.rw=Rook(4,4,self.board,'white')
        self.wb=Bishop(1,1,self.board,'white')
        self.board[self.rw.pos[0]][self.rw.pos[1]]=self.rw
        self.board[self.wb.pos[0]][self.wb.pos[1]]=self.wb

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

    def make_moves(self):
        user=input()
        user.lower()
        
        user=user.split(' ')
        piece=user[0]
        piece_start_pos= user[1]
        pos_input=user[3]
        pos=self.rw.pos
        print(user)
        if piece=='rook':
            print('rook')
            piece=self.rw
           
            
            self.board=piece.move(self.board,piece,pos_input)
            
            
            if piece.pos[0]<0:
                print('error')
            elif piece.pos[1]<0:
                print('error')
                
            else:
                self.display_update()
        if piece=='bishop':
            piece=self.wb
            
            self.board=self.wb.move(self.board,piece,pos_input)
            

            if self.wb.pos[0]<0:
                print('error')
            elif self.wb.pos[1]<0:
                print('error')
            else:
                self.display_update()

    def display_update(self):
        #play
        # print(self.board)
        for line in self.board:
            for square in line:
                if isinstance(square,Piece):
                    print ('object')
      
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

    


bored=Board()
bored.display_update()
bored.game_loop()