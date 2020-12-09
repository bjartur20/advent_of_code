def get_data():
    with open('9\input.txt') as f:
        data = f.read().split("\n")
    f.close()

    return data

def binary_search(arr, val):
    low = 0
    high = len(arr) - 1

    return binary_search_recur(arr, low, high, val)

def binary_search_recur(arr, low, high, val):
    if high >= low:
        mid = low + (high - low) // 2 # Get the middle index of arr

        # Check if val is in the middle
        if arr[mid] == val:
            return mid
        elif arr[mid] > val:
            # Search right part of arr
            return binary_search_recur(arr, low, mid - 1, val)
        else:
            # Search left part of arr
            return binary_search_recur(arr, mid + 1, high, val)
    else:
        # Val not found in arr
        return -1

def verify_num(i, nums):
    nums.sort()
    for n in nums:
        x = i - n
        res = binary_search(nums, x)
        if res != -1:
            return True
    
    return False

def part_one(nums):
    preamble = nums[:25]
    i = nums[25]

    if not verify_num(i, preamble):
        return i
    
    return part_one(nums[1:])


def part_two(xmas, invalid_num):
    cont_range = []
    for i in xmas:
        cont_range.append(i)
        if sum(cont_range) == invalid_num:
            return max(cont_range) + min(cont_range)
        if sum(cont_range) > invalid_num:
            return part_two(xmas[1:], invalid_num)

def main():
    data = get_data()
    data = [int(i) for i in data]

    p1 = part_one(data)
    p2 = part_two(data, p1)

    print(f"Part one: {p1}")
    print(f"Part two: {p2}")

if __name__ == "__main__":
    main()