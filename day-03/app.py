from aocd.models import Puzzle
puzzle = Puzzle(year=2021, day=3)


def problem_1(lines):
	row_count = len(lines.split())
	index_count = len(lines.split()[0])
	print(f'Row count: { row_count }')
	print(f'Indexes: { index_count }')

	# setup lists
	bit_ones = [0 * i for i in range(index_count)]
	gamma_binary=[0 * i for i in range(index_count)]
	epsilon_binary=[0 * i for i in range(index_count)]

	# For every line
	# Every index in that line, counter 1's in the bit_ones list
	for line in lines.split():
		for i in range(0, len(bit_ones)):
			if int(line[i]) == 1:
				bit_ones[i] += 1


	print(f'Ones: { bit_ones }')

	# Zeroes are opposite: 
	# For every index, substract (rowcount - count of ones) to get zeroes count
	bit_zeroes = [row_count - i for i in bit_ones]
	print(f'Zeroes: { bit_zeroes }')


	# Evaluate the common value 0 vs 1 for each index
	# Commons equate to gamma list
	# Min values assigned to epsilon (opposite of gamma index values)
	for idx in range(index_count):
		if bit_ones[idx] > bit_zeroes[idx]:
			gamma_binary[idx] = "1"
			epsilon_binary[idx] = '0'
		elif bit_zeroes[idx] > bit_ones[idx]:
			gamma_binary[idx] = "0"
			epsilon_binary[idx] = "1"

	print(f'Gamma Binary: { gamma_binary }')
	print(f'Epsilong Binary: { epsilon_binary }')

	# Convert string binary to int
	gamma_rate = int(''.join(gamma_binary),2)
	print(f'Gamma Rate: { gamma_rate } ')

	epsilon_rate = int(''.join(epsilon_binary), 2)
	print(f'Epsilon Rate: { epsilon_rate } ')

	# Multiply Gamma and Epsilon int values
	power_consuption = gamma_rate * epsilon_rate

	print(f'Power Consumption: { power_consuption }')


problem_1(puzzle.input_data)
