from tkinter import *
import random

GAME_WIDTH = 600
GAME_HEIGHT = 400
GAME_SPEED = 100  # milliseconds
SPACE_SIZE = 20 # Size of each space in the grid (20x20 px)
BODY_PARTS = 3  # Initial length of the snake
SNAKE_COLOR = "#B40583"
FOOD_COLOR = "#00FF00"
BACKGROUND_COLOR = "#000000"

class Snake:   # Represents the snake in the game. Handles snake position, movement and growth.
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.square = []

        for i in range(BODY_PARTS):
            self.coordinates.append([0, 0])  # Initial position of the snake
        
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag='snake')
            self.square.append(square)

class Food:    # Represents the food in the game. Handle the random generation of food.
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH - SPACE_SIZE) // SPACE_SIZE) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT - SPACE_SIZE) // SPACE_SIZE) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag='food')

def next_turn():
    # Logic to determine the next turn for the snake
    pass

def change_direction(new_direction):
    # Logic to change the direction of the snake
    pass

def check_collisions():
    # Logic to check for collisions with walls or food
    pass

def game_over():
    # Logic to handle game over conditions
    pass

window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down' # Initial direction of the snake

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")  # Set the window size and position
snake = Snake()
food = Food()

window.mainloop()