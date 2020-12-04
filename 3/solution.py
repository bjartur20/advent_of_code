TREE = "#"

def get_input():
    input_list = []
    input_file = open('3\input.txt')
    for line in input_file:
        input_list.append(line.strip())
    input_file.close()

    return input_list

def extend_hill(hill):
    for i in range(0, len(hill)):
        hill[i] *= 100

def part_one(hill, slope):
    right, down = slope
    line_length = len(hill[0])
    trees = 0
    y_cord = 0
    x_cord = 0

    # Check heach line in the hill for trees
    while y_cord != 322:
        # Change the coordinates
        x_cord += right
        y_cord += down

        # Out of range check
        try:
            # Check if we find a tree at the cordinates
            if hill[y_cord][x_cord] == TREE:
                trees += 1
        except Exception as e:
            print("Aagh out of the map!")
            print("Exception:", e)
            return trees

    return trees

def part_two(hill, slopes):
    res = 1

    for slope in slopes:
        res *= part_one(hill, slope)

    return res

def main():
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    hill = get_input()
    extend_hill(hill)
    trees = part_one(hill, slopes[1])
    num = part_two(hill, slopes)

    print(f"Part one: {trees}")
    print(f"Part one: {num}")

if __name__ == "__main__":
    main()