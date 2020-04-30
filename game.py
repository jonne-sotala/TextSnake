from board import Board

class Game(object):
    def __init__(self):
        self.board = Board()


    def next(self, x):
        if x == 'w':
            self.board.snake.direction = "up"
        elif x == 'a':
            self.board.snake.direction = "left"
        elif x == 'd':
            self.board.snake.direction = "right"
        elif x == 's':
            self.board.snake.direction = "down"

        self.board.snake.move()
        if not self.board.check_state():
            print("The snake died and you lost!")
            return False

        return True



    