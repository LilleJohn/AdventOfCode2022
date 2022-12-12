
def main():
    with open('day4\\assignments.txt') as f:
        lines = f.readlines()
    print(get_number_of_contained(lines, fully_contained=True)) # Part 1
    print(get_number_of_contained(lines, fully_contained=False)) # Part 2


def get_number_of_contained(lines: list, fully_contained: bool) -> int:
    number_of_contained = 0

    for line in lines:
        elf_pair = pair_min_max(line)
        if fully_contained and is_fully_contained(elf_pair):
                number_of_contained = number_of_contained + 1
        elif not fully_contained and is_partially_contained(elf_pair):
                number_of_contained = number_of_contained + 1
    return number_of_contained


def pair_min_max(line: str) -> tuple:
    first_hyphon = line.find("-")
    second_hyphon = line.find("-", first_hyphon+1)
    comma = line.find(",")

    elf_one_min_max = [line[:first_hyphon], line[first_hyphon+1:comma]]
    if line.find("\n") == -1:
        elf_two_min_max = [line[comma+1:second_hyphon], line[second_hyphon+1:]]
    else:
        elf_two_min_max = [line[comma+1:second_hyphon], line[second_hyphon+1:-1]]
    return elf_one_min_max, elf_two_min_max


def is_fully_contained(elf_pair: tuple) -> bool:
    elf_one, elf_two = elf_pair

    # Is elf_one contained in elf_two?
    if int(elf_one[0]) >= int(elf_two[0]) and int(elf_one[1]) <= int(elf_two[1]):
        return True
    # Is elf_two contained in elf_one?
    elif int(elf_one[0]) <= int(elf_two[0]) and int(elf_one[1]) >= int(elf_two[1]):
        return True
    return False


def is_partially_contained(elf_pair: tuple) -> bool:
    elf_one, elf_two = elf_pair

    # Is elf_one at all a part in elf_two?
    if int(elf_one[1]) < int(elf_two[0]) or int(elf_one[0]) > int(elf_two[1]):
        return False
    return True


if __name__ == "__main__":
    main()
