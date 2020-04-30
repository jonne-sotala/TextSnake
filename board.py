from snake import Snake
from food import Food
import random

class Board(object):

    "Board of the game"
    def __init__(self, n=10, m=10):
        self.EMPTY = " "
        self.SNAKE = "o"
        self.BORDER = "X"
        self.FOOD = "A"
        self.food = Food(-1, -1)
        self.grid = [self.EMPTY] * (n+2)
        # Fill in the borders
        for i in range(n+2):
            self.grid[i] = [self.EMPTY] * (m+2)
        for i in range(m+2):
            self.grid[0][i] = self.BORDER
            self.grid[-1][i] = self.BORDER
        for i in range(n+2):
            self.grid[i][0] = self.BORDER
            self.grid[i][-1] = self.BORDER
        self.snake = Snake(5, 5, "left")
        # Fill in the snake
        self.grid[self.snake.locationX][self.snake.locationY] = self.SNAKE
        for snakebody in self.snake.body:
            self.grid[snakebody.locationX][snakebody.locationY] \
                = self.SNAKE
        # Add in the food
        self.new_food()

    def new_food(self):
        while True:
            x = random.randrange(1, len(self.grid)-1)
            y = random.randrange(1, len(self.grid[0])-1)
            if self.grid[x][y] == self.EMPTY:
                self.food = Food(x, y)
                self.grid[self.food.locationX][self.food.locationY] = self.FOOD
                break

    def move_snake(self):
        for i in range(1, len(self.grid)-1):
            for j in range(1, len(self.grid[0])-1):
                if (self.grid[i][j] == self.SNAKE):
                    self.grid[i][j] = self.EMPTY
        self.grid[self.snake.locationX][self.snake.locationY] = self.SNAKE
        for snakebody in self.snake.body:
            self.grid[snakebody.locationX][snakebody.locationY] \
                = self.SNAKE


    def check_state(self):
        if self.grid[self.snake.locationX][self.snake.locationY] == self.EMPTY:
            self.move_snake()
            return True
        
        if self.grid[self.snake.locationX][self.snake.locationY] == self.BORDER:
            return False
        elif self.grid[self.snake.locationX][self.snake.locationY] == self.SNAKE:
            return False
        elif self.grid[self.snake.locationX][self.snake.locationY] == self.FOOD:
            self.move_snake()
            self.snake.eat()
            self.new_food()
            return True
        

    def show_state(self):
        str = ""
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                str = str + self.grid[i][j] + " "
            if i < len(self.grid)-1:
                str = str + "\n"
        print(str)