#========================================================
#
#   Visit the website for the functioning of code:
#   https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
#
#========================================================

#   functions to define the robots movement

#   turn_right() function sets the robot to turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#   the function below moves the robot until it reaches the goal
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()