def get_input():
    with open('6\input.txt') as f:
        data = f.read().split("\n\n")
    f.close()

    return data

def part_one(group):
    return len(set.union(*map(set, group.splitlines())))

def part_two(group):
    return len(set.intersection(*map(set, group.splitlines())))

def main():
    data = get_input()

    c1, c2 = 0, 0
    for group in data:
        c1 += part_one(group)
        c2 += part_two(group)

    print(f"Part one: {c1}")
    print(f"Part two: {c2}")

if __name__ == "__main__":
    main()