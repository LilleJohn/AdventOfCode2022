import re


def main():
    with open('day3\inventory.txt') as f:
        lines = f.readlines()

    priority = 0
    for line in lines:
        denominator = find_common_denominator(line)
        priority = priority + calc_line_priority(denominator)
    print(priority) # Part 1

    groups = create_groups(lines)
    badges = find_badges(groups)
    print(calc_badge_priority(badges)) # Part 2


def find_common_denominator(line: str) -> str:
    first_half = line[:int(len(line)/2)]
    second_half = line[int(len(line)/2):]

    for item in first_half:
        if re.search(item, second_half):
            return item


def calc_line_priority(denominator: str) -> int:
    if denominator.islower():
        return ord(denominator) - 96 # ASCII character "a" has dec value 97
    return ord(denominator) - 38 # ASCII character "A" has dec value 65


def create_groups(lines:list) -> list:
    groups = []
    for i in range(0, len(lines), 3):
        groups.append(lines[i:i+3])
    return groups


def find_badges(groups: list) -> list:
    badges = []
    for group in groups:
        for item in group[0]:
            if re.search(item, group[1]) and re.search(item, group[2]):
                badges.append(item)
                break
    return badges


def calc_badge_priority(badges: list) -> int:
    priority = 0
    for badge in badges:
        priority = priority + calc_line_priority(badge)
    return priority


if __name__ == "__main__":
    main()
