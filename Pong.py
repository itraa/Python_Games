# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 1] # pixels per update (1/60 seconds)


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists

#    set initial ball position to be center of canvas
    ball_pos[0] = WIDTH / 2
    ball_pos[1] = HEIGHT / 2
    ball_vel = [0,1]

    ball_vel[0] = random.randrange(120/60, 240/60)
    ball_vel[1] = random.randrange(60/60, 180/60)

    if direction == LEFT:
# set initial velocity to be upward left
        ball_vel[0] = -ball_vel[0]
        ball_vel[1] = -ball_vel[1]
    else:  # direction == RIGHT
# set initial velocity to be upward right
        ball_vel[1] = -ball_vel[1]      

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    paddle1_pos = 200
    paddle2_pos = 200
    paddle1_vel = 0
    paddle2_vel = 0
    direction = random.choice([LEFT,RIGHT])
    spawn_ball(direction)
    
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
         
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # collide and reflect off of top and bottom of wall
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]

    if ball_pos[1] >= (HEIGHT - 1)-BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    
    # collide and reflect off of left and right hand side of canvas

    if ball_pos[0] >= WIDTH-PAD_WIDTH-BALL_RADIUS:
        if ball_pos[1] in range(paddle2_pos - HALF_PAD_HEIGHT, paddle2_pos + HALF_PAD_HEIGHT):
            ball_vel[0] *= 1.1
            ball_vel[0] = -ball_vel[0] 
        else:
            score1 += 1
            spawn_ball(LEFT)
    elif ball_pos[0] <= BALL_RADIUS+PAD_WIDTH:
        if ball_pos[1] in range(paddle1_pos - HALF_PAD_HEIGHT, paddle1_pos + HALF_PAD_HEIGHT):
            ball_vel[0] *= 1.1
            ball_vel[0] = -ball_vel[0]
        else:
            score2 += 1           
            spawn_ball(RIGHT)

    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_vertical_pos = paddle1_pos + paddle1_vel
    paddle2_vertical_pos = paddle2_pos + paddle2_vel

    if paddle1_vertical_pos <= (HEIGHT - HALF_PAD_HEIGHT) and paddle1_vertical_pos >= HALF_PAD_HEIGHT:
        paddle1_pos += paddle1_vel
    if paddle2_vertical_pos <= (HEIGHT - HALF_PAD_HEIGHT) and paddle2_vertical_pos >= HALF_PAD_HEIGHT:
        paddle2_pos += paddle2_vel
    
    # draw paddles
    x_pos = 3
    left_top_point = [x_pos, paddle1_pos - HALF_PAD_HEIGHT] 
    left_bottom_point = [x_pos, paddle1_pos + HALF_PAD_HEIGHT]

    c.draw_line(left_top_point, left_bottom_point, PAD_WIDTH, 'Blue')     
    
    y_pos = 596
    right_top_point = [y_pos, paddle2_pos - HALF_PAD_HEIGHT] 
    right_bottom_point = [y_pos, paddle2_pos + HALF_PAD_HEIGHT]

    c.draw_line(right_top_point, right_bottom_point, PAD_WIDTH, 'Blue')

    # draw scores
    c.draw_text(str(score1),[150,100], 30, "White", "monospace")
    c.draw_text(str(score2),[450,100], 30, "White", "monospace")

def keydown(key):
    global paddle1_vel, paddle2_vel

    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= 4
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += 4
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += 4
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= 4        

def keyup(key):
    global paddle1_vel, paddle2_vel
        
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0        


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
label = frame.add_label("Let's play a game of Pong! \n", 200)
label = frame.add_label("                           \n", 200)

Reset = frame.add_button('Restart',new_game, 75)

# start frame
new_game()
frame.start()
