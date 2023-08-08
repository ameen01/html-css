import pygame
import random

# Set up Pygame
pygame.init()

# Set up the game window
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")

# Set up the colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the snake
snake_speed = 15
snake_size = 15

# Set up the food
food_size = 15

# Set up the game loop
clock = pygame.time.Clock()
running = True

# Set up the snake class
class Snake:
  def __init__(self):
    self.x = screen_width // 2
    self.y = screen_height // 2
    self.dx = 0
    self.dy = 0
    self.body = [(self.x, self.y)]

  def update(self):
    # Update the snake's position
    self.x += self.dx
    self.y += self.dy

    # Keep the snake within the screen bounds
    if self.x < 0:
      self.x = screen_width - snake_size
    elif self.x > screen_width - snake_size:
      self.x = 0
    if self.y < 0:
      self.y = screen_height - snake_size
    elif self.y > screen_height - snake_size:
      self.y = 0

    # Update the snake's body
    self.body.insert(0, (self.x, self.y))
    self.body.pop()

  def draw(self):
    # Draw the snake's body
    for x, y in self.body:
      pygame.draw.rect(screen, white, (x, y, snake_size, snake_size))

# Set up the food class
class Food:
  def __init__(self):
    self.x = random.randrange(0, screen_width, food_size)
    self.y = random.randrange(0, screen_height, food_size)

  def draw(self):
    # Draw the food
    pygame.draw.rect(screen, white, (self.x, self.y, food_size, food_size))

# Create the snake and food
snake = Snake()
food = Food()

# Main game loop
while running:
  # Handle events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        snake.dx = -snake_speed
        snake.dy = 0
      elif event.key == pygame.K_RIGHT:
        snake.dx = snake_speed
        snake.dy = 0
      elif event.key == pygame.K_UP:
        snake.dx = 0
        snake.dy = -snake_speed
      elif event.key == pygame.K_DOWN:
