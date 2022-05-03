

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
        self.pieces_covered=[]
        
class Pawn(Piece):
    def __init__(self,col,row,board,color):
        Piece.__init__(self,col,row,board,color)
        self.first_turn=True
        if self.color=='white':
            self.letter='P'
        else:
            self.letter='p'


    def move(self,board,pos_input):
        self.last_move=tuple(self.pos)
        self.get_possible_moves(board)
        if tuple(position_lookup[pos_input]) not in self.possible_moves:
            raise Invalid_move()
        board[self.pos[0]][self.pos[1]]='.'
        self.pos=position_lookup[pos_input] 
        board[self.pos[0]][self.pos[1]]=self
        self.first_turn=False
        
        return board
    def get_possible_moves(self,board):
        self.start_pos=tuple(self.pos)
        self.possible_moves=[]
        move_amount=0
        if self.first_turn:
            move_amount=2
        else:
            move_amount=1
        if self.color=='black':
            for i in range (move_amount):
                self.pos[0]+=1
                self.possible_moves.append(tuple(self.pos))
            move_amount=0
        else:
            for i in range(move_amount):
                self.pos[0]-=1
                self.possible_moves.append(tuple(self.pos))
            move_amount=0
       
        self.pos=[self.start_pos[0],self.start_pos[1]]
        return self.possible_moves
                
            
    def make_move(self,board,pos_input):
        try:
                board=self.move(board,pos_input)
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

    def move(self,board,pos_input):
        self.get_possible_moves(self,board)
        print(f"{tuple(position_lookup[pos_input])} is the coord of the square you want to move to")
        if tuple(position_lookup[pos_input]) not in self.possible_moves:
            raise Invalid_move()
            
                
        self.last_move=board[self.pos[0]][self.pos[1]]
        board[self.pos[0]][self.pos[1]]='.'
        self.pos=position_lookup[pos_input]
        
        board[self.pos[0]][self.pos[1]]=self
        
        return board


    def get_possible_moves(self,board):
        self.start_pos=tuple(self.pos)
        
    
        up=True
        down=False
        left=False
        right=False
        
        while up:
            if self.pos[0]>=7:
                up=False
                down=True
            else:
                self.pos[0]-=1
                coord=tuple(self.pos)
                self.possible_moves.append(tuple(self.pos))
                if isinstance((board.get_piece(coord)),Piece):
                    print('found a piece')
                    right=False
                    left=True
                    if board[coord[0]][coord[1]].color==self.color:
                        
                        self.pieces_covered.append(coord)

                    else:
                        self.possible_moves.append(coord)
                if self.pos[0]<=0:
                    self.pos=[self.start_pos[0],self.start_pos[1]]
                    up=False
                    down=True
                
        while down:
            if self.pos[0]>=7:
                down=False
                left=True
            else:
                self.pos[0]+=1
                coord=tuple(self.pos)
                self.possible_moves.append(tuple(self.pos))
                if isinstance(self.pos,Piece):
                    print('found a piece')
                    right=False
                    left=True
                    if board.get_piece(coord).color==self.color:
                        self.possible_moves.remove(coord)
                        self.pieces_covered.append(coord)
                    else:
                        self.possible_moves.append(coord)
                if self.pos[0]>=7:
                    self.pos=[self.start_pos[0],self.start_pos[1]]
                    down=False
                    left=True
        while left:
            if self.pos[1]<=0:
                left=False
                right=True
            else:
                self.pos[1]-=1
                coord=tuple(self.pos)
                
                #if isinstance((board.board[self.pos[0][self.pos[1]]]),Piece):
                if isinstance(board.get_piece(self.pos),Piece):
                    print('found a piece')
                    right=False
                    left=True
                    if board.get_piece(coord).color==self.color:
                        self.pieces_covered.append(coord)
                    else:
                        self.possible_moves.append(coord)
                else:
                    self.possible_moves.append(coord)
                if self.pos[1]<=0:
                    self.pos=[self.start_pos[0],self.start_pos[1]]
                    left=False
                    right=True
        while right:
            if self.pos[1]>=7:
                right=False
            else:
                self.pos[1]+=1
                coord=tuple(self.pos)
                
                if isinstance(self.pos,Piece):
                    print('found a piece')
                    right=False
                    left=True
                    if board.get(coord).color==self.color:
                        self.pieces_covered.append(coord)
                    else:
                        self.possible_moves.append(coord)
                if self.pos[1]==7:
                    self.pos=[self.start_pos[0],self.start_pos[1]]
                    right=False
        
        self.pos=[self.start_pos[0],self.start_pos[1]]
        for coord in self.possible_moves:
            if isinstance(self.pos,Piece):
                if board[coord[0]][coord[1]].color==self.color:
                    self.possible_moves.remove(coord)
                    self.pieces_covered.append(coord)
        info_lists=[self.possible_moves,self.pieces_covered]
        return info_lists
    def make_move(self,board,pos_input):
        try:
            board=self.move(board,pos_input)
            return board
        except Invalid_move as err:
            print("Invalid",err)
            # Do something...
            raise err

class Knight(Piece):
    def __init__(self,col,row,board,color) -> None:
        Piece.__init__(self,col,row,board,color)
        self.name='knight'
        if self.color=='white':
            self.letter='N'
        else:
            self.letter='n'
    def move(self,board,pos_input):
        self.last_move=board[self.pos[0]][self.pos[1]]
        self.get_possible_moves(self,board)
        if tuple(position_lookup[pos_input]) not in self.possible_moves:
            raise Invalid_move()
        board[self.pos[0]][self.pos[1]]='.'
        self.pos=position_lookup[pos_input] 
        board[self.pos[0]][self.pos[1]]=self
        return board
    def get_possible_moves(self,board):
        self.start_pos=tuple(self.pos)
        self.possible_moves.append((self.pos[0]+2,self.pos[1]+1))
        self.pos=self.start_pos
        self.possible_moves.append((self.pos[0]+2,self.pos[1]-1))
        self.pos=self.start_pos
        self.possible_moves.append((self.pos[0]+1,self.pos[1]+2))
        self.pos=self.start_pos
        self.possible_moves.append((self.pos[0]+1,self.pos[1]-2))
        self.pos=self.start_pos
        self.possible_moves.append((self.pos[0]-2,self.pos[1]+1))
        self.pos=self.start_pos
        self.possible_moves.append((self.pos[0]-2,self.pos[1]-1))
        self.pos=self.start_pos
        self.possible_moves.append((self.pos[0]-1,self.pos[1]+2))
        self.pos=self.start_pos
        self.possible_moves.append((self.pos[0]-1,self.pos[1]-2))

        for coord in self.possible_moves[:]:
            if isinstance(coord,Piece):
                    if board[coord[0]][coord[1]].color==self.color:
                        self.possible_moves.remove(coord)
                        self.selfs_covered.append(coord)

            elif coord[0]>7 or coord[0]<0:
                self.possible_moves.remove(coord)

            elif coord[1]>7 or coord[1]<0:
                self.possible_moves.remove(coord)
        return board
    def make_move(self,board,pos_input):
        try:
            board=self.move(board,pos_input)
            return board
        except Invalid_move as err:
            print('caught invalid move',err)
            print('handle it???')
            return board


class Bishop(Piece):
    def __init__(self,col,row,board,color) -> None:
        Piece.__init__(self,col,row,board,color)
        self.name='bishop'
        if self.color=='white':
            self.letter='B'
        else:
            self.letter='b'


    def move(self,board,pos_input):
        self.last_move=board[self.pos[0]][self.pos[1]]
        self.get_possible_moves(self,board)
        if tuple(position_lookup[pos_input]) not in self.possible_moves:
            raise Invalid_move()
        board[self.pos[0]][self.pos[1]]='.'
        self.pos=position_lookup[pos_input] 
        board[self.pos[0]][self.pos[1]]=self

        return board
    def get_possible_moves(self,board) :
        self.start_pos=tuple(self.pos)
        up=True
        down=False
        right=True
        left=False 
        while up and right:
            if self.pos[0]<=0 or self.pos[1]<=0:
                right=False
                left=True
            else:

                self.pos[0]-=1
                self.pos[1]-=1
                coord=tuple(self.pos)
                if isinstance(self.pos,Piece):
                    print('found a piece')
                    right=False
                    left=True
                    if board[coord[0]][coord[1]].color==self.color:
                        self.possible_moves.remove(coord)
                        self.pieces_covered.append(coord)
                    else:
                        self.possible_moves.append(coord)
                else:       
                    self.possible_moves.append(tuple(self.pos))
                if self.pos[0]<=0 or self.pos[1]<=0:
                    self.pos=[self.start_pos[0],self.start_pos[1]]
                    right=False
                    left=True
        while up and left:
            if self.pos[0]<=0 or self.pos[1]>=7:
                down=True
                up=False
            else:
                self.pos[0]-=1
                self.pos[1]+=1
                coord=tuple(self.pos)
                if isinstance(self.pos,Piece):
                    if board[coord[0]][coord[1]].color==self.color:
                        self.possible_moves.remove(coord)
                        self.selfs_covered.append(coord)
                        down=True
                        up=False
                else:
                    self.possible_moves.append(tuple(self.pos))
                if self.pos[0]<=0 or self.pos[1]>=7:
                    self.pos=[self.start_pos[0],self.start_pos[1]]
                    down=True
                    up=False

        while down and left:
            if self.pos[0]>=7 or self.pos[1]>=7:
                left=False
                right=True
            else:
                self.pos[0]+=1
                self.pos[1]+=1
                coord=tuple(self.pos)
                if isinstance(board.get(coord),Piece):
                    print('found a piece')
                    if board[coord[0]][coord[1]].color==self.color:
                        self.pieces_covered.append(coord)
                        right=True
                        left=False
                else:  
                     self.possible_moves.append(tuple(self.pos))
                if self.pos[0]>=7 or self.pos[1]>=7:
                    self.pos=[self.start_pos[0],self.start_pos[1]]
                    left=False
                    right=True
        while down and right:
            if self.pos[0]>=7 or self.pos[1]<=0:
                right=True
                left=False
                break
                
            else:
                self.pos[0]+=1
                self.pos[1]-=1
                coord=tuple(self.pos)
                if isinstance(self.pos,Piece):
                    if board[coord[0]][coord[1]].color==self.color:
                        self.possible_moves.remove(coord)
                        self.pieces_covered.append(coord)
                        right=True
                        left=False
                else:
                    self.possible_moves.append(tuple(self.pos))
                if self.pos[0]>=7 or self.pos[1]<=0:
                    self.pos=[self.start_pos[0],self.start_pos[1]]
                    down=False
                    right=False
        for coord in self.possible_moves:
            if isinstance(self.pos,Piece):
                if board[coord[0]][coord[1]].color==self.color:
                    self.possible_moves.remove(coord)
                    self.pieces_covered.append(coord)
        info_lists=[self.possible_moves,self.pieces_covered]
        return info_lists
    def make_move(self,board,pos_input):
        try:
            board=self.move(board,pos_input)
            return board
        except Invalid_move as err:
            print('caught invalid move',err)
            print('handle it???')
            return board

class Queen(Piece):
    def __init__(self,col,row,board,color):
        Piece.__init__(self,col,row,board,color)
        self.name='Queen'
        if self.color=='white':
            self.letter='Q'
        else:
            self.letter='q'
    def move(self,board,pos_input):
        self.last_move=self.pos
        self.get_possible_moves(board)
        if tuple(position_lookup[pos_input]) not in self.possible_moves:
            raise Invalid_move()
        board.board[self.pos[0]][self.pos[1]]='.'
        self.pos=position_lookup[pos_input] 
        print(self.pos)
        board.board[self.pos[0]][self.pos[1]]=self
        return board

    def get_possible_moves(self,board):
        info_lst1=Rook.get_possible_moves(self,board)
        info_lst2=Bishop.get_possible_moves(self,board)
        move_lst1=info_lst1[0]
        move_lst2=info_lst2[0]
        print(info_lst2)
        print(move_lst1)
        print(move_lst2)
        #self.possible_moves=move_lst1+move_lst2
        #self.pieces_covered=info_lst1[1]+info_lst2[1]
        print(self.possible_moves)
        
        for coord in self.possible_moves[:]:
            if isinstance(self.pos,Piece):
                if board[coord[0]][coord[1]].color==self.color:
                    self.possible_moves.remove(coord)
        return self.possible_moves
    def make_move(self,board,pos_input):
        try:
            board=self.move(board,pos_input)
            return board
        except Invalid_move as err:
            print('caught invalid move',err)
            print('handle it???')
            return board
class King(Piece): 
    def __init__(self,col,row,board,color) -> None:
        Piece.__init__(self,col,row,board,color)
        self.name=' king'
        if self.color=='white':
            self.letter='K'
        else:
            self.letter='k'
        self.check=False
        self.checkmate=False
    def get_possible_moves(self,board):
        start_coord=tuple(self.pos)
        self.possible_moves.append((start_coord[0]+1,start_coord[1]))
        self.possible_moves.append((start_coord[0],start_coord[1]+1))
        self.possible_moves.append((start_coord[0]+1,start_coord[1]+1))
        self.possible_moves.append((start_coord[0]-1,start_coord[1]+1))
        self.possible_moves.append((start_coord[0]+1,start_coord[1]-1))
        self.possible_moves.append((start_coord[0],start_coord[1]-1))
        self.possible_moves.append((start_coord[0]-1,start_coord[1]))
        self.possible_moves.append((start_coord[0]-1,start_coord[1]-1))
        print(self.possible_moves)
        for coord in self.possible_moves[:]:
            
            if coord[0]>=8:
                self.possible_moves.remove(coord)
            elif coord[1]>=8:
                 self.possible_moves.remove(coord)
            elif coord[0]<=0:
                self.possible_moves.remove(coord)
            elif coord[1]<=0:
                 self.possible_moves.remove(coord)
        print(self.possible_moves)
        for coord in self.possible_moves[:]:
            if isinstance(self.pos,Piece):
                if board[coord[0]][coord[1]].color==self.color:
                    self.possible_moves.remove(coord)
            
        
        return self.possible_moves
    def move(self,board,pos_input):
        self.last_move=board[self.pos[0]][self.pos[1]]
        self.get_possible_moves(board)
        if tuple(position_lookup[pos_input]) not in self.possible_moves:
            raise Invalid_move()
        board[self.pos[0]][self.pos[1]]='.'
        self.pos=position_lookup[pos_input] 
        board[self.pos[0]][self.pos[1]]=self
    
class Board:
    def __init__ (self):
       
        self.board=[ ["."] * 8 for i in range(8)]
        self.turn='white'
        self.x_change=False
        self.y_change=False
        self.direction=0
        self.test=False
    turn_dict={
        'w':'white',
        'b':'black'}
    black_pieces={
        'r':Rook,
        'b':Bishop,
        'n':Knight,
        'k':King,
        'q':Queen,
        'p':Pawn
    }
    white_pieces={
        'R':Rook,
        'B':Bishop,
        'N':Knight,
        'K':King,
        'Q':Queen,
        'P':Pawn
    }
    def setup(self,fen):
        info=fen.split(' ')
        board_info=info[0]
        turn_info=info[1]
        self.turn=self.turn_dict[turn_info]
        ranks=board_info.split('/')
        if len(ranks)!= 8:
            raise ValueError('invalid fen')
        for rn,rank in enumerate(ranks):
            file=0
            for letter in rank:
                if letter in self.black_pieces:
                    piece=self.black_pieces[letter](rn,file,self.board,'black')
                    file += 1
                    self.board[piece.pos[0]][piece.pos[1]]=piece
                    #self.display_update()
                elif letter in self.white_pieces:
                    
                    piece=self.white_pieces[letter](rn,file,self.board,'white')
                    self.board[piece.pos[0]][piece.pos[1]]=piece
                    #self.display_update()
                    file += 1
                else:
                    file += 1
    
    def get_fen(self):
        row_lst=[]
        fen_lst=[]
        counter=0
        counter_2=0
        
        for row in self.board:
            if len(row_lst)>= 8:
                   fen_lst.append(''.join(row_lst))
                   row_lst=[]
                
            if counter<8:
                if counter>0:
                    row_lst.append(str(counter))
            if counter==8:

                fen_lst.append(str(counter))
            counter=0
            fen_lst.append(''.join(row_lst))
            row_lst=[]
            for square in row:
                
                
                if isinstance(square,Piece):
                    if counter>0 and counter<8:
                        row_lst.append(str(counter))
                        counter=0
                    row_lst.append(square.letter)

                else: 
                      counter+=1 
        fen_lst.append(''.join(row_lst))
        row_lst=[]
        for i in fen_lst[:]:
            if i=='':
                fen_lst.remove(i)  
                                  
        fen='/'.join(fen_lst)
        return fen


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
    def get_piece(self,pos):
        piece=self.board[pos[0]][pos[1]]

    def make_moves_for_text (self, user):
        user.lower()
        user=user.split(' ')
        pos=user[0]
        
        pos_input=user[2]
        
        
        piece=position_lookup[pos]
        piece=self.board[piece[0]][piece[1]]
        print(piece.color)
        if piece.color!=self.turn:
            raise Invalid_move
        if isinstance (piece,Piece):
            
            piece.make_move(self,pos_input)
        else: 
            raise Invalid_move()

        if self.turn=='white':
            self.turn='black'
        else:
            self.turn='white'
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

def test_text_ui ():
    board = Board()
    board.make_moves_for_text('g8 to a8')
    board.display_update()
    board.make_moves_for_text('h7 ot g8')
    board.display_update()
    
    #board.make_moves_for_text('bishop d2 to e8')
def test_possible_queen_moves():
    board=Board()
    queen=board.board[7][6]
    print(queen.get_possible_moves(board))
def test_king():
    board=Board()
    board.wk=King(7,7,board,'white')
    queen=board.board[7][6]
    board.board[board.wk.pos[0]][board.wk.pos[1]]=board.wk
    board.board[7][7]
    board.board[7][6].get_possible_moves(queen,board.board)
    
    print(board.board[7][6].pieces_covered)
    #print(board.wk.get_possible_moves(board.wk,board.board))
    board.display_update()
    
def test_knight():
    board=Board()
    board.wn=Knight(7,7,board,'white')
    board.board[board.wn.pos[0]][board.wn.pos[1]]=board.wn

    board.display_update()
    board.wn.get_possible_moves(board)
    print(board.wn.possible_moves)
def test_board_setup():
    board=Board()
    board.setup('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq')
    board.display_update()
    print(board.get_fen())

def test_get_fen():
    board=Board()
    board.setup('rnbqkbnr/pppppppp/8/8/1n6/8/PPPPPPPP/RNBQKBNR')
    print(board.get_fen())
#this is wher I will run all of my tests
#test_possible_queen_moves()
#test_text_ui()
#test_king()
#test_knight()
#test_board_setup()
#test_fen()
#test_get_moves()
bored=Board()
bored.setup('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq')
bored.display_update()
bored.game_loop()