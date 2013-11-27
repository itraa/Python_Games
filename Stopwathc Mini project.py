# template for "Stopwatch: The Game"

import simplegui
import time

# define global variables
number = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"


# define event handler for timer with 0.1 sec interval
def increment_number():
    global number
    number = number + 1
    print number
    
timer = simplegui.create_timer(100, increment_number)

# define draw handler
def draw(canvas):
    canvas.draw_text(str(time.time()),[150, 150], 24, "White")

# create frame
frame = simplegui.create_frame("Stopwatch Game!", 300, 300)

# register draw handler    
frame.set_draw_handler(draw)

# register event handlers


# start frame
timer.start()
frame.start()

# Please remember to review the grading rubric
