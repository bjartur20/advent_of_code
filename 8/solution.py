def get_data():
    with open('8\input.txt') as f:
        data = f.read().split("\n")
    f.close()

    return data

def command_parser(data):
    commands = [line.split(" ") for line in data]
    return commands

def loop_finder(commands):
    '''Finds the loop in the commands code.

    Args:
        commands (list): list of lists inlcuding operations and arguments

    Returns:
        tuple: A typle including the acc variable at the start of the loop, 
               looped boolean which tells if the code looped or not,
               and the indexes of code before the loop.
    '''

    old = []
    acc = 0
    idx = 0
    looped = False
    # Go through the list of commands
    while idx < len(commands):
        curr = commands[idx]
        op, arg = curr[0], int(curr[1])

        # Loop checker
        if idx in old:
            looped = True
            break

        old.append(idx)
        if op == "acc":
            acc += arg
            idx += 1
        elif op == "jmp":
            idx += arg
        else:
            idx += 1

    return acc, looped, old

def part_one(commands):
    acc, looped, old = loop_finder(commands)
    return acc, old

def part_two(old, commands):
    '''Modifies the code to eliminate the loop by changing a single
       operation in the commands code.

    Args:
        old (list): List of indexes of the code before the first loop.
        commands (list): List of lists including the original code.

    Returns:
        acc (int): The acc variable at the end of the code with no loops.
    '''

    # Loops through the indexes of the commands before the original loop
    for i in old:
        op, arg = commands[i]
        saved = commands[i] # Save the original version of the command to be replaced
        
        # Try changing the command if it's a jump or no-op
        if op == "jmp":
            commands[i] = ["nop", arg]
        elif op == "nop":
            commands[i] = ["jmp", arg]

        test = loop_finder(commands) # Check if the code still contains a loop
        acc = test[0]
        # If the loop has not been eliminated, change the command back to the original one
        if test[1]:
            commands[i] = saved
        else:
            break

    return acc

def main():
    raw_data = get_data()
    commands = command_parser(raw_data)
    
    p1 = part_one(commands)
    p2 = part_two(p1[1], commands)

    print(f"Part one: {p1[0]}")
    print(f"Part two: {p2}")

if __name__ == "__main__":
    main()