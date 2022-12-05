

def main() -> None:
    with open('day1\calories.txt') as f:
        lines = f.readlines()
    print(f"Part 1: {max(sum_elfs(lines))}")
    print(f"Part 2: {sum_three_max(sum_elfs(lines))}")


def sum_elfs(lines: list) -> list:
    elfs = []
    current = 0
    for i in range(len(lines)):
        if len(lines[i]) > 1 or lines[i].find("\n") == -1:
            current = current + int(lines[i])
        if i == len(lines) or len(lines[i]) == 1:
            elfs.append(current)
            current = 0
    return elfs


def sum_three_max(elfs: list) -> int:
    max_total = 0
    for _ in range(3):
        max_total = max_total + max(elfs)
        elfs.pop(elfs.index(max(elfs)))
    return max_total


if __name__ == "__main__":
    main()
