# Will make Reeborg's World robot spin around,
# hugging and moving along walls
# or going straight if there is no wall.
def turn_right():
    turn_left()
    turn_left()
    turn_left()
# This will jump over small walls 
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
# This will jump over small walls 
def hop():
    if wall_in_front() == True:
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
    else:
        move()
# This will climb up any wall until it reaches the top 
def big_wall():
    if wall_in_front() == True:
        turn_left()
    else:
        move()
# This, paired with big_wall(), will descent any wall when the top is reached
# if at_goal() is true, then you win
# So you will spin around walls until you win. 
def down():
    while wall_in_front() == False:
        if at_goal() == True:
            done()
        else:
            move()
            turn_right()
# This will just walk if no wall is in front; if a wall is reached, big_wall() will begin
def walk():
    while front_is_clear():
        move()
# Spin around walls
number_of_hurdles = 100
for hurdles in range(number_of_hurdles):
    if at_goal() == True:
        done()
    elif not at_goal():
        walk()
        big_wall()
        down()
