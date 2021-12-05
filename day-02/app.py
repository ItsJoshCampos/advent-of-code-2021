from aocd.models import Puzzle
puzzle = Puzzle(year=2021, day=2)

def problem_1(input_data):
	x_coor = 0
	y_coor = 0

	# add/subtract coordinates
	for line in input_data.split('\n'):
		cmd = line.split(' ')
		if cmd[0] == 'forward':
			x_coor += int(cmd[1])
		elif cmd[0] == 'up':
			y_coor -= int(cmd[1])
		elif cmd[0] == 'down':
			y_coor += int(cmd[1])

	# find product
	coor_product = x_coor * y_coor

	print(f'X Coordinate: {x_coor}')
	print(f'Y Coordinate: {y_coor}')
	print(f'X * Y = {coor_product}')


def problem_2(input_data):
	x_coor = 0
	y_coor = 0
	aim = 0

	# add/subtract coordinates
	for line in input_data.split('\n'):
		cmd = line.split(' ')
		if cmd[0] == 'forward':
			x_coor += int(cmd[1])
			y_coor += (aim * int(cmd[1]))
		elif cmd[0] == 'up':
			aim -= int(cmd[1])
		elif cmd[0] == 'down':
			aim += int(cmd[1])

	# find product
	coor_product = x_coor * y_coor

	print(f'X Coordinate: {x_coor}')
	print(f'Y Coordinate: {y_coor}')
	print(f'X * Y = {coor_product}')

problem_1(puzzle.input_data)
problem_2(puzzle.input_data)