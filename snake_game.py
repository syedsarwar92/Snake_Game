from sense_hat import SenseHat
import time, random


sense = SenseHat()

red = (255, 0, 0)
green = (0, 255, 0)
nothing = (0,0,0)

snake = [[3, 3]] # snake starting position
direction = [1, 0] # moving direction
length = 1 # current length of the snake


foodPos = [random.randint(0,7), random.randint(0,7)] # first random food position

pixels = [nothing] * 64



def setDirection(d): # 0 = up, 1 = right, 2 = down, 3 = left
  
  global direction
  
  if d == 0:
    direction = [0, -1]
  elif d == 1:
    direction = [1, 0]
  elif d == 2:
    direction = [0, 1]
  elif d == 3:
    direction = [-1, 0]

sense.show_message("Snake Game")

while True:
  
  
  pixels = [nothing] * 64
  
  
  
  for event in sense.stick.get_events():  # joystick events
    
    if event.action == "pressed":  # actions are- pressed, held and released
     
      if event.direction == "up":
        if length > 1:  
          if direction == [0, 1]:
            setDirection(2)
          else:
            setDirection(0)
        else:
            setDirection(0)
     
      elif event.direction == "right":
        if length > 1:
          if direction == [-1, 0]:
            setDirection(3)
          else:
            setDirection(1)
        else:
         setDirection(1)
      
      elif event.direction == "down":
        if length > 1:
          if direction == [0, -1]:
            setDirection(0)
          else:
            setDirection(2)
        else:
         setDirection(2)
      
      elif event.direction == "left":
        if length > 1:
          if direction == [1, 0]:
            setDirection(1)
          else:
            setDirection(3)
        else:
          setDirection(3)
  
  snake.insert(0, [snake[0][0] + direction[0], snake[0][1] + direction[1]])
   
  if snake[0][0] < 0:  # game boundaries
    sense.show_message("Game Over")
    x = "Score: " +  str(len(snake) - 2)
    sense.show_message(x)
    break
  if snake[0][1] < 0:
    sense.show_message("Game Over")
    x = "Score: " +  str(len(snake) - 2)
    sense.show_message(x)
    break
  if snake[0][0] > 7:
    sense.show_message("Game Over")
    x = "Score: " +  str(len(snake) - 2)
    sense.show_message(x)
    break
  if snake[0][1] > 7:
    sense.show_message("Game Over")
    x = "Score: " +  str(len(snake) - 2)
    sense.show_message(x)
    break
  
  if sense.get_temperature() <= -10 or sense.get_temperature() >= 60:  # temperature
    sense.show_message("Game Over")
    x = "Score: " +  str(len(snake) - 2)
    sense.show_message(x)
    break
  
  if snake[0] == foodPos:   # if snake eats food
    foodPos = []
    while foodPos ==[]:
      foodPos = [random.randint(0,7), random.randint(0,7)]
      if foodPos in snake:
        foodPos = []
    length += 1
    
  elif snake[0] in snake[1:]:  # if snake bites itself
    sense.show_message("Game Over")
    x = "Score: " +  str(len(snake) - 2)
    sense.show_message(x)
    break
    
  else:
    while len(snake) > length:
      snake.pop()
  
  for pos in snake:
    pixels[pos[1] * 8 + pos[0]] = green
  
  pixels[foodPos[1] * 8 + foodPos[0]] = red  #y * rowSize + x, covert 2D coordinate into 1D coordinate for foodPos
  sense.set_pixels(pixels)
  snake_speed = 0.1*(len(snake) -2)
  if snake_speed < 0.8:
    time.sleep(1 - 0.1*(len(snake) -2))
  else:
    time.sleep(0.2)
  
  