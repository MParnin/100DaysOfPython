def turn_right():
	turn_left()
	turn_left()
	turn_left()

while not at_goal():
	if front_is_clear():
		move()
	if right_is_clear():
		turn_right()
	if wall_in_front() and wall_on_right():
		turn_left()