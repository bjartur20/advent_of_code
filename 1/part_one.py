NUMBER = 2020

def get_input():
    input_list = []
    input_file = open('1\input.txt')
    for line in input_file:
        input_list.append(int(line))
    input_file.close()

    return input_list

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

if __name__ == "__main__":
    input_list = get_input()
    input_list.sort()

    for n in input_list:
        num = NUMBER - n

        res = binary_search(input_list, num)
        if res != -1:
            print(input_list[res] * n)
            break
