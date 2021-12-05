from aocd.models import Puzzle
puzzle = Puzzle(year=2021, day=1)

# Option to read from input file
# with open('input.txt', 'r') as r:
#     lines = r.readlines()

# Set as list of integers
int_list = list(map(int, puzzle.input_data.splitlines()))


def problem_1(depths):
    """Count the number of times a depth measurement increases from the previous measurement.
    Answer should be 1167
    """

    count = 0
    # Read out first index value
    previous_depth = depths[0]

    # Start on second index value
    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            count += 1

    return count


def problem_2(depths):
    """Consider sums of a three-measurement sliding window.
    How many sums are larger than the previous sum?
    Answer should be 1130
    """

    count = 0
    # First depth sum
    previous_depth = depths[0] + depths[1] + depths[2]

    # Start on second index value
    for i in range(1, len(depths) - 1):
        # Sum of 3 measurement window
        curr_depth = depths[i - 1] + depths[i] + depths[i + 1]
        if curr_depth > previous_depth:
            count += 1

        previous_depth = curr_depth

    return count


print(problem_1(int_list))
print(problem_2(int_list))
