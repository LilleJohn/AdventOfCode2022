import re


# Part 1
# A, X = Rock
# B, Y = Paper
# C, Z = Scissor

# Part 2
# X = Lose
# Y = Draw
# Z = Win

def part_one(lines: list) -> None:
    total_points = 0
    for line in lines:
        outcome = get_outcome_p1(line)
        total_points = total_points + calc_points_p1(line, outcome)
    print(total_points) #Part 1


def get_outcome_p1(line: str) -> int:
    """Returns point value for outcome. 6p for win, 3p for draw and 0p for loss"""
    if (re.search("A", line) and re.search("Y", line)) or (re.search("B", line) and re.search("Z", line)) or (re.search("C", line) and re.search("X", line)):
        return 6
    elif (re.search("A", line) and re.search("Z", line)) or (re.search("B", line) and re.search("X", line)) or (re.search("C", line) and re.search("Y", line)):
        return 0
    else:
        return 3


def calc_points_p1(line:str, outcome: int) -> int:
    points = outcome
    if re.search("X", line):
        points = points + 1
    elif re.search("Y", line):
        points = points + 2
    elif re.search("Z", line):
        points = points + 3
    return points


def part_two(lines: list) -> None:
    points = 0
    for line in lines:
        outcome = get_outcome_p2(line)
        points = points + calc_points_p2(outcome, line)
    print(points) #Part 2


def get_outcome_p2(line: str) -> int:
    if re.search("Y", line):
        return 3
    elif re.search("Z", line):
        return 6
    return 0


def calc_points_p2(outcome: int, line: str) -> int:
    if outcome == 6:
        if re.search("A", line):
            return outcome + 2
        elif re.search("B", line):
            return outcome + 3
        elif re.search("C", line):
            return outcome + 1
    elif outcome == 3:
        if re.search("A", line):
            return outcome + 1
        elif re.search("B", line):
            return outcome + 2
        elif re.search("C", line):
            return outcome + 3
    elif outcome == 0:
        if re.search("A", line):
            return outcome + 3
        elif re.search("B", line):
            return outcome + 1
        elif re.search("C", line):
            return outcome + 2


if __name__ == "__main__":
    with open('day2\strategy.txt') as f:
        lines = f.readlines()
    part_one(lines)
    part_two(lines)
