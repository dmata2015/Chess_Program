

class Rook:
    def __init__(self,col,row,board,color) -> None:
        self.pos=[row,col]
        self.board=board
        self.color=color
class Bishop:
    def __init__(self,col,row,board,color) -> None:
        self.pos=row,col
        self.board=board
        self.color=color
        
class King: 
    def __init__(self,col,row,board,color) -> None:
        self.pos=row,col
        self.board=board
        self.color=color
class Board:
    def __init__ (self):
        self.display_board = [ ["."] * 8 for i in range(8)]
        self.board=[ ["."] * 8 for i in range(8)]
        self.x_change=False
        self.y_change=False
        #print(self)
        self.rw=Rook(4,4,self.board)
        self.wb=Bishop(1,1,self.board)
        self.display_board[self.wb.pos[0]][self.wb.pos[1]]='B'
        self.display_board[self.rw.pos[0]][self.rw.pos[1]]='R'
        self.board[self.rw.pos[0]][self.rw.pos[1]]=self.rw
    def get_fov(self,piece)->tuple:
        pass
    def game_loop(self):
        running = True
        
        while running:
            
            user_input=input()
            if user_input.lower()=='play':
                
                self.make_moves()
            if user_input.lower()=='stop':
                running=False

    def make_moves(self):
        user=input()
        user.lower()
        
        user=user.split(' ')
        piece=user[0]
        print(user)
        if piece=='rook':
            print('rook')
            if user[1]=='forward'or user[1]=='backwards':
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
            if self.y_change:
                self.display_board[self.rw.pos[0]][self.rw.pos[1]]="."
                self.display_board[self.rw.pos[0] - (self.direction * int(user[2]))][self.rw.pos[1]]='R'
                
                self.board[self.rw.pos[0]][self.rw.pos[1]]="."
                self.board[self.rw.pos[0] - (self.direction * int(user[2]))][self.rw.pos[1]]=self.rw
                self.rw.pos=[(self.rw.pos[0] - (self.direction * int(user[2]))),self.rw.pos[1]]

                print(self.rw.pos)
                self.display_update()
            if self.x_change:
                self.display_board[self.rw.pos[0]][self.rw.pos[1]]="."
                self.display_board[self.rw.pos[0]][self.rw.pos[1] - (self.direction * int(user[2]))]='R'
                
                self.board[self.rw.pos[0]][self.rw.pos[1]]="."
                self.board[self.rw.pos[0]][self.rw.pos[1] - (self.direction * int(user[2]))]=self.rw
                self.rw.pos=[self.rw.pos[0],(self.rw.pos[1] - (self.direction * int(user[2])))]
                self.display_update()
                if self.rw.pos[0]<0:
                    print('error')
            if self.rw.pos[1]<0:
                print('error')
                self.display_update()
        if piece=='bishop':
            y_negative_change=False
            x_negative_change=False
            if user[1]=='down':
                y_negative_change=True
            if user[1]=='left':
                x_negative_change=True
            
            if y_negative_change and x_negative_change:
                
            

   
    def display_update(self):
        foo=0
        print("  A B C D E F G H")
        for i in self.display_board:
            foo+=1
            print(foo,'|'.join(i))
            
    
    
bored=Board()
bored.display_update()
bored.game_loop()