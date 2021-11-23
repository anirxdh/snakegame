
from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVEMENT = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

#they are constants so they are in all caps

class Snake():

    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # creating snake body

        for index in STARTING_POSITIONS:
            self.add_segment(index)

    def add_segment(self,index):
            box = Turtle("square")
            box.color("white")
            box.penup()
            box.goto(index)
            self.segments.append(box)

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):

    # movement of snake body

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVEMENT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)