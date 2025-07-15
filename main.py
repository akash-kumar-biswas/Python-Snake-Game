from tkinter import *
import random

GAME_WIDTH = 600
GAME_HEIGHT = 400
GAME_SPEED = 120  # milliseconds
SPACE_SIZE = 20 # Size of each space in the grid (20x20 px)
BODY_PARTS = 3  # Initial length of the snake
SNAKE_COLOR = "#07ABC8"
FOOD_COLOR = "#AE04FD"
BACKGROUND_COLOR = "#004D17"

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

def next_turn(snake, food):
    # Logic to determine the next turn for the snake
    x, y = snake.coordinates[0]

    if direction == 'up':
        y -= SPACE_SIZE
    elif direction == 'down':
        y += SPACE_SIZE
    elif direction == 'left':
        x -= SPACE_SIZE
    elif direction == 'right':
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y)) 
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag='snake')
    snake.square.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:  # Check if snake eats the food
        global score
        score += 1   
        label.config(text="Score:{}".format(score))
        canvas.delete('food')
        food = Food()  
    else:  # If food is not eaten, remove the last segment of the snake   
        del snake.coordinates[-1]  
        canvas.delete(snake.square[-1]) 
        del snake.square[-1]

    if check_collisions(snake):  
        game_over()
    else:
        window.after(GAME_SPEED, next_turn, snake, food)

def change_direction(new_direction):
    # Logic to change the direction of the snake
    global direction

    if new_direction == 'left' and direction != 'right':
        direction = new_direction
    elif new_direction == 'right' and direction != 'left':
        direction = new_direction
    elif new_direction == 'up' and direction != 'down':
        direction = new_direction
    elif new_direction == 'down' and direction != 'up':
        direction = new_direction

def check_collisions(snake):
    # Logic to check for collisions with walls or food
    x, y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True
    
    for body_part in snake.coordinates[1:]:  # Check if snake collides with itself
        if x == body_part[0] and y == body_part[1]:
            return True
    return False

def game_over():
    # Logic to handle game over conditions
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('Arial', 30), text="Game Over",  fill="#C70909", tag='game_over')
    

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

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()