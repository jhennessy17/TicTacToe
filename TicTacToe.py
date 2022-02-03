#Jeremiah Hennessy 4108453
import random

#Class of game board
class Board:
    def __init__(self):
        self.spot = []
        for x in range(0,9):
            self.spot.append(' ')
            
    def show(self):
        print(self.spot[6] + ' | ' + self.spot[7] + ' | ' + self.spot[8])
        print('----------')
        print(self.spot[3] + ' | ' + self.spot[4] + ' | ' + self.spot[5])
        print('----------')
        print(self.spot[0] + ' | ' + self.spot[1] + ' | ' + self.spot[2])

    def free(self, num):
        return self.spot[num] == ' '

    def full(self):
        for x in range(0,9):
            if(self.spot[x] == ' '):
                return 0
        return 1

#Class for a player object
class player:
    def __init__(self):
        self.letter = ''
        self.choice = -1
        
    def choose_letter(self):
        while not (self.letter == 'X' or self.letter == 'O'):
            self.letter = raw_input("Choose your letter(X or O): ").upper()

    def player_move(self, Board):
        while (self.choice < 0 or self.choice > 8):
            x = raw_input("Choose a spot(1-9 counting left to right bottom left is 1): ")
            self.choice = int(x)
            self.choice -= 1
        if not (Board.free(self.choice)):
            self.choice = -1
            self.player_move(Board)
    
    #Random move of computer
    def cpu_rand_move(self, Board):
        open_spots = []
        for x in range(0,9):
            if(Board.free(x)):
                open_spots.append(x)
        return random.choice(open_spots)
    
    #Block opponent and work for three in a row
    def cpu_ai_move(self, player, Board):
        for x in range (0,9):
            if not(Board.spot[x] == player.letter or Board.spot[x] == self.letter):
                Board.spot[x] = self.letter
                if(self.win(Board)):
                    Board.spot[x] = ' '
                    return x
                else:
                    Board.spot[x] = ' '
        for x in range (0,9):
            if not(Board.spot[x] == player.letter or Board.spot[x] == self.letter):
                Board.spot[x] = player.letter
                if(player.win(Board)):
                    Board.spot[x] = ' '
                    return x
                else:
                    Board.spot[x] = ' '

        return self.cpu_rand_move(Board)


    def win(self, Board):
        return ((Board.spot[6] == self.letter and Board.spot[7] == self.letter and Board.spot[8] == self.letter)
                or (Board.spot[3] == self.letter and Board.spot[4] == self.letter and Board.spot[5] == self.letter)
                or (Board.spot[0] == self.letter and Board.spot[1] == self.letter and Board.spot[2] == self.letter)
                or (Board.spot[6] == self.letter and Board.spot[3] == self.letter and Board.spot[0] == self.letter)
                or (Board.spot[7] == self.letter and Board.spot[4] == self.letter and Board.spot[1] == self.letter)
                or (Board.spot[8] == self.letter and Board.spot[5] == self.letter and Board.spot[2] == self.letter)
                or (Board.spot[0] == self.letter and Board.spot[4] == self.letter and Board.spot[8] == self.letter)
                or (Board.spot[6] == self.letter and Board.spot[4] == self.letter and Board.spot[2] == self.letter))

class Game:
    def beginner(self):
        board = Board()
        p1 = player()
        p2 = player()
        p1.choose_letter()
        if(p1.letter == 'X'):
            p2.letter = 'O'
        else:
            p2.letter = 'X'
        x = ''
        while not(x == 'yes' or x == 'no'):
            x = raw_input('Would you like to go first(yes or no): ')
        if(x == 'yes'):
            while not(p1.win(board) or p2.win(board) or board.full()):
                board.show()
                p1.player_move(board)
                board.spot[p1.choice] = p1.letter
                if not(p1.win(board) or p2.win(board) or board.full()):
                    board.spot[p2.cpu_rand_move(board)] = p2.letter
                    p1.choice = -1
        else:
            while not(p1.win(board) or p2.win(board) or board.full()):
                board.spot[p2.cpu_rand_move(board)] = p2.letter
                if not(p1.win(board) or p2.win(board) or board.full()):
                    board.show()
                    p1.player_move(board)
                    board.spot[p1.choice] = p1.letter
                    p1.choice = -1
        board.show()
        if(p1.win(board)):
            print('Congratulations you won!')
        elif(p2.win(board)):
            print('Sorry you lost')
        else:
            print('Looks like a tie')

    def expert(self):
        board = Board()
        p1 = player()
        p2 = player()
        p1.choose_letter()
        if(p1.letter == 'X'):
            p2.letter = 'O'
        else:
            p2.letter = 'X'
        x = ''
        while not(x == 'yes' or x == 'no'):
            x = raw_input('Would you like to go first(yes or no): ')
        if(x == 'yes'):
            while not(p1.win(board) or p2.win(board) or board.full()):
                board.show()
                p1.player_move(board)
                board.spot[p1.choice] = p1.letter
                if not(p1.win(board) or p2.win(board) or board.full()):
                    board.spot[p2.cpu_ai_move(p1, board)] = p2.letter
                    p1.choice = -1
        else:
            while not(p1.win(board) or p2.win(board) or board.full()):
                board.spot[p2.cpu_ai_move(p1, board)] = p2.letter
                if not(p1.win(board) or p2.win(board) or board.full()):
                    board.show()
                    p1.player_move(board)
                    board.spot[p1.choice] = p1.letter
                    p1.choice = -1
        board.show()
        if(p1.win(board)):
            print('Congratulations you won!')
        elif(p2.win(board)):
            print('Sorry you lost')
        else:
            print('Looks like a tie')

    def play(self):
        print('Welcome to Tic Tac Toe')
        x = ""
        while not(x == 'beginner' or x == 'expert' or x == 'Beginner' or x == 'Expert'):
            x = raw_input('Would you like Beginner or Expert difficulty(type beginner or expert): ')
        if(x == 'beginner' or x == 'Beginner'):
            self.beginner()
        else:
            self.expert()

game = Game()
game.play()



