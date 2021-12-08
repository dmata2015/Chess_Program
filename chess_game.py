
class Piece:
    def __init__(self,row,col,board,color) -> None:
        self.pos=[row,col]
        self.board=board
        self.color=color
class Rook(Piece):
    def __init__(self,col,row,board,color) -> None:
        self.pos=[row,col]
        self.value=5
        self.board=board
        self.color=color
        self.name='rook'
        self.letter='R'
    def move(self,y_change,user,direction,piece,board,display_board):
        if y_change:
            display_board[piece.pos[0]][piece.pos[1]]="."
            display_board[piece.pos[0] - (direction * int(user[2]))][piece.pos[1]]='R'
            
            board[piece.pos[0]][piece.pos[1]]="."
            board[piece.pos[0] - (direction * int(user[2]))][piece.pos[1]]=piece
            piece.pos=[(piece.pos[0] - (direction * int(user[2]))),piece.pos[1]]
        else:
            display_board[piece.pos[0]][piece.pos[1]]="."
            display_board[piece.pos[0]][piece.pos[1] - (direction * int(user[2]))]='R'
            board[piece.pos[0]][piece.pos[1]]="."
            board[piece.pos[0]][piece.pos[1] - (direction * int(user[2]))]=piece
            piece.pos=[piece.pos[0],(piece.pos[1] - (direction * int(user[2])))]
        print(display_board)
        return board
class Bishop(Piece):
    def __init__(self,col,row,board,color) -> None:
        Piece.__init__(self,col,row,board,color)
        self.name='bishop'
        self.letter='B'
        
    def move(self,y_negative_change,x_negative_change,user,piece,board,display_board) :
        if y_negative_change and x_negative_change:
            print('down left')
            board[piece.pos[0]][piece.pos[1]]='.'
            board[piece.pos[0]+int(user[3])][piece.pos[1]-int(user[3])]=piece

            display_board[piece.pos[0]][piece.pos[1]]='.'
            display_board[piece.pos[0]+int(user[3])][piece.pos[1]-int(user[3])]='B'
            

        elif y_negative_change and not x_negative_change:
            print('down right')
            board[piece.pos[0]][piece.pos[1]]='.'
            board[piece.pos[0]+int(user[3])][piece.pos[1]+int(user[3])]=piece

            display_board[piece.pos[0]][piece.pos[1]]='.'
            display_board[piece.pos[0]+int(user[3])][piece.pos[1]+int(user[3])]='B'
            y_negative_change=False
            x_negative_change=False
            
        elif not y_negative_change and x_negative_change:
            print('up left')
            board[piece.pos[0]][piece.pos[1]]='.'
            board[piece.pos[0]-int(user[3])][piece.pos[1]-int(user[3])]=piece

            display_board[piece.pos[0]][piece.pos[1]]='.'
            display_board[piece.pos[0]-int(user[3])][piece.pos[1]-int(user[3])]='B'
            y_negative_change=False
            x_negative_change=False

        elif not y_negative_change and not x_negative_change:
            print('up right')
            board[piece.pos[0]][piece.pos[1]]='.'
            board[piece.pos[0]-int(user[3])][piece.pos[1]+int(user[3])]=piece

            display_board[piece.pos[0]][piece.pos[1]]='.'
            display_board[piece.pos[0]-int(user[3])][piece.pos[1]+int(user[3])]='B'
        return [board,display_board]
class King(Piece): 
    def __init__(self,col,row,board,color) -> None:
        self.pos=[row,col]
        self.board=board
        self.color=color

class Board:
    def __init__ (self):
        self.display_board = [ ["."] * 8 for i in range(8)]
        self.board=[ ["."] * 8 for i in range(8)]
        self.x_change=False
        self.y_change=False
        #print(self)
        self.direction=0
        self.test=False
        self.rw=Rook(4,4,self.board,'white')
        self.wb=Bishop(1,1,self.board,'white')
        self.display_board[self.wb.pos[0]][self.wb.pos[1]]='B'
        self.display_board[self.rw.pos[0]][self.rw.pos[1]]='R'
        self.board[self.rw.pos[0]][self.rw.pos[1]]=self.rw
        self.board[self.wb.pos[0]][self.wb.pos[1]]=self.wb
    def get_fov(self,piece)->tuple:
        pass


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
        pos=self.rw.pos
        print(user)
        if piece=='rook':
            print('rook')
            piece=self.rw
            if user[1]=='up'or user[1]=='down':
                self.y_change=True
                if user[1]=='backwards':
                    self.direction=-1
                else:
                    self.direction=1
            if user[1]=='right'or user[1]=='left':
                self.x_change=True
                self.y_change=False
                if user[1]=='left':
                    self.direction=1
                else:
                    self.direction=-1
           
            
            new_stage=piece.move(self.y_change,user,self.direction,piece,self.board,self.display_board)[0]
            self.board=new_stage[0]
            self.display_board=new_stage[1]
            
            if piece.pos[0]<0:
                print('error')
            elif piece.pos[1]<0:
                print('error')
                
            else:
                self.display_update()
        if piece=='bishop':
            piece=self.wb
            y_negative_change=False
            x_negative_change=False
            if user[1]=='down':
                y_negative_change=True
            if user[2]=='left':
                x_negative_change=True
            print(y_negative_change)
            print(x_negative_change)

            

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
      
        print("   A B C D E F G H")
        for rn,row in enumerate(self.board):
            print(rn+1,end='')
            for square in row:
                
                if isinstance(square,Piece):
                    
                    print (square.letter,end='')
                    
                else:
                    print(square,end='')
                print('|',end='')
            print('')
    def check_for_take(self):
        pass


def test_rook():
    bored=Board()
    bored.display_update()

    


bored=Board()
bored.display_update()
bored.game_loop()