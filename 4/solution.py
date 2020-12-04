import re

def get_input():
    with open('4\input.txt') as f:
        data = f.read().split("\n\n")
    f.close()

    data = [entry.replace("\n", " ").split(" ") for entry in data]

    for i in range(len(data)):
        data[i] = {data[i][j][:3]: data[i][j][4:] for j in range(len(data[i]))}

    return data

def part_one(passport):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    counter = 0
    for field in required_fields:
        if field in passport:
            counter += 1
    
    return 1 if counter == 7 else 0

def part_two(passport):
    # Nr of fields
    if (7 == len(passport) and 'cid' not in passport) or len(passport) == 8:
        # Birth year
        if 1920 <= int(passport['byr']) <= 2002:
            # Issue year
            if 2010 <= int(passport['iyr']) <= 2020:
                # Expiration year
                if 2020 <= int(passport['eyr']) <= 2030:
                    # Hair color
                    if passport['hcl'][0] == "#" and re.match('[a-f0-9]', passport['hcl'][1:]):
                        # Eye color
                        if passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                            # Passport ID
                            if passport['pid'].isnumeric() and len(passport['pid']) == 9:
                                # Height
                                if passport['hgt'][-2:] == 'cm':
                                    if 150 <= int(passport['hgt'][:-2]) <= 193:
                                        return True
                                elif passport['hgt'][-2:] == 'in':
                                    if 59 <= int(passport['hgt'][:-2]) <= 76:
                                        return True

    return False

def main():
    p1_counter, p2_counter = 0, 0
    data = get_input()

    for passport in data:
        p1_counter += part_one(passport)
        p2_counter += part_two(passport)
    
    print(f"Part one: {p1_counter}")
    print(f"Part two: {p2_counter}")

if __name__ == "__main__":
    main()
