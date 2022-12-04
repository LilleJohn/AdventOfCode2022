

def first_task(lines: list) -> int:
    current = 0
    max = 0

    for line in lines:
        if len(line) > 1:
            current = current + int(line)
        else:
            if current > max:
                max = current
            current = 0
    return max


def second_task(lines: list) -> int:
    current = 0
    elfs = []
    max_total = 0

    for i in range(len(lines)):
        if len(lines[i]) > 1 or lines[i].find("\n") == -1:
            current = current + int(lines[i])
        if i == len(lines) or len(lines[i]) == 1:
            elfs.append(current)
            current = 0
    
    for _ in range(3):
        max_total = max_total + max(elfs)
        elfs.pop(elfs.index(max(elfs)))

    return max_total


if __name__ == "__main__":

    with open('day1\calories.txt') as f:
        lines = f.readlines()

    # with open('day1\\test.txt') as f:
    #     lines = f.readlines()

    print(first_task(lines))
    print(second_task(lines))
