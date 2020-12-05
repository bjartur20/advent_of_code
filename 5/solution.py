def get_input():
    with open('5\input.txt') as f:
        data = [line.strip() for line in f]
    f.close()

    return data

def binary_space_partitioning(instructions, low, high):
    mid = low + (high - low) // 2
    
    if len(instructions) == 0:
        return mid

    elif instructions[0] in "FL":
        return binary_space_partitioning(instructions[1:], low, mid)
    else:
        return binary_space_partitioning(instructions[1:], mid+1, high)

def seat_id_converter(seat):
    row = binary_space_partitioning(seat[:7], 0, 127)
    col = binary_space_partitioning(seat[7:], 0, 7)

    return row * 8 + col

# seat id converter (Gudjon)
# def calcSeatID (inputString):
#     rowID = int(inputString[:7].replace("F", "0").replace("B", "1"), 2)
#     colID = int(inputString[7:].replace("L", "0").replace("R", "1"), 2)
#     return rowID * 8 + colID


def part_one(seat_ids):
    return max(seat_ids)

def part_two(seat_ids):
    seat_ids.sort()
    print(seat_ids)
    for idx, seat in enumerate(seat_ids):
        if seat + 1 != seat_ids[idx+1]:
            return seat + 1

def main():
    data = get_input()
    seat_ids = [seat_id_converter(seat) for seat in data]
    p1 = part_one(seat_ids)
    p2 = part_two(seat_ids)

    print(f'Part one: {p1}')
    print(f'Part two: {p2}')

if __name__ == "__main__":
    main()