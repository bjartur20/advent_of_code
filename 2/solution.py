def get_input():
    input_list = []
    input_file = open('2\input.txt')
    for line in input_file:
        input_list.append(line.strip())
    input_file.close()

    return input_list

def parse_passwords(pass_raw):
    password_list = []

    for passw in pass_raw:
        tokens = passw.rstrip().split(" ")
        first, second = map(int, tokens[0].split("-"))
        letter = tokens[1][0]
        password = tokens[2]

        password_list.append((first, second, letter, password))

    return password_list

def part_one(password):
    first, second, special_letter, passw = password 

    if int(first) <= passw.count(special_letter) <= int(second):
        return 1
    
    return 0

def part_two(password):
    first, second, special_letter, passw = password 

    if (passw[first - 1] == special_letter) != (passw[second - 1] == special_letter):
        return 1
    
    return 0

def count_valid_passwords(password_list):
    one, two = 0, 0
    for line in password_list:
        one += part_one(line)
        two += part_two(line)
    
    return one, two

def main():
    pass_raw = get_input()
    password_list = parse_passwords(pass_raw)
    counters = count_valid_passwords(password_list)
    print(f"Part one: {counters[0]}\nPart two: {counters[1]}")

if __name__ == "__main__":
    main()