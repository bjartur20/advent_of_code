NUMBER = 2020

def get_input():
    input_list = []
    input_file = open('1\input.txt')
    for line in input_file:
        input_list.append(int(line))
    input_file.close()

    return input_list

def solution(arr, num):
    res = []

    for i in range(len(arr) - 2):
        if i > num and arr[i] == arr[i - 1]:
            continue

        low = i + 1
        high = len(arr) - 1

        while low < high:
            sum = arr[i] + arr[low] + arr[high]

            if sum < num:
                low += 1
            elif sum > num:
                high -= 1
            else:
                res.append(arr[i])
                res.append(arr[low])
                res.append(arr[high])
            
                while low < len(arr) - 1 and arr[low] == arr[low + 1]:
                    low += 1
                while high > 0 and arr[high] == arr[high - 1]:
                    high -= 1
                low += 1
                high -= 1

    return res

if __name__ == "__main__":
    input_list = get_input()
    input_list.sort()

    res = solution(input_list, NUMBER)
    print(res[0] * res[1] * res[2])
