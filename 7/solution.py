def get_data():
    with open('7\input.txt') as f:
        data = f.read().split("\n")
    f.close()

    return data

def parse_rules(rules):
    rules_dict = {}
    for rule in rules:
        outer, inner = rule.split(" bags contain")
        inner_bags = inner.lstrip().rstrip(".").split(", ")

        rules_dict[outer] = []
        if "no other" in inner:
            continue
        
        for bag in inner_bags:
            times, color1, color2, *_ = bag.split(" ")
            rules_dict[outer] += [f"{color1} {color2}"] * int(times)

    return rules_dict

def part_one(rules, bag):
    bag_colors = set()

    for outer, inner in rules.items():
        if bag in inner:
            bag_colors.add(outer)
            bag_colors.update(part_one(rules, outer))

    return bag_colors

def part_two(rules, bag):
    counter = 0

    for inner in rules[bag]:
        counter += 1 + part_two(rules, inner)
    
    return counter

def main():
    rules_raw = get_data()
    rules_dict = parse_rules(rules_raw)
    
    p1 = len(part_one(rules_dict, "shiny gold"))
    p2 = part_two(rules_dict, "shiny gold")

    print(f"Part one: {p1}")
    print(f"Part two: {p2}")

if __name__ == "__main__":
    main()