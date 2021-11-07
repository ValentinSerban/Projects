from turtle import Turtle
import random

FOOD_SHAPES = ["turtle", "circle", "square"]
FOOD_COLOR = ["red", "blue", "yellow", "orange", "green", "purple", "white"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(random.choice(FOOD_SHAPES))
        self.penup()
        self.shapesize(0.5)
        self.color(random.choice(FOOD_COLOR))
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.shape(random.choice(FOOD_SHAPES))
        self.color(random.choice(FOOD_COLOR))
        self.goto(random_x, random_y)
