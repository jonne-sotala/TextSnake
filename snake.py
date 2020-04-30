from snakebody import SnakeBody

class Snake(object):

    "The snake in the game"
    def __init__(self, locationX, locationY, direction, length=3):
        self.locationX = locationX
        self.locationY = locationY
        self.direction = direction
        self.justAte = False
        self.body = []
        for i in range(1, length+1):
            if self.direction == "left":
                bodypart = SnakeBody(locationX, locationY+i)
            elif self.direction == "up":
                bodypart = SnakeBody(locationX+i, locationY)
            elif self.direction == "right":
                bodypart = SnakeBody(locationX, locationY-i)
            else:
                bodypart = SnakeBody(locationX-i, locationY)
            self.body.append(bodypart)

    def move(self):
        if self.justAte:
            self.grow()
            self.justAte = False
        else:
            self.move_body()

        if self.direction == "left":
            self.locationY = self.locationY - 1
        elif self.direction == "up":
            self.locationX = self.locationX - 1
        elif self.direction == "right":
            self.locationY = self.locationY + 1
        else:
            self.locationX = self.locationX + 1

    def eat(self):
        self.justAte = True

    def grow(self):
        self.body.append(SnakeBody(self.body[-1].locationX, 
                                   self.body[-1].locationY))
        for i in range(len(self.body)-2, 0, -1):
            self.body[i].locationX = self.body[i-1].locationX
            self.body[i].locationY = self.body[i-1].locationY
        self.body[0].locationX = self.locationX
        self.body[0].locationY = self.locationY
        # After this the snake will always move its head
        # forward so the body and head won't stay on top of each other.

    def move_body(self):
        for i in range(len(self.body)-1, 0, -1):
            self.body[i].locationX = self.body[i-1].locationX
            self.body[i].locationY = self.body[i-1].locationY
        self.body[0].locationX = self.locationX
        self.body[0].locationY = self.locationY
        # After this the snake will always move its head
        # forward so the body and head won't stay on top of each other.
