def sum_array(arr):
    if arr == None or len(arr) <= 2:
        return 0
    else:
        for i in range(len(arr)):
            min = i
            for pivo in range(i + 1, len(arr)):
                if arr[pivo] < arr[min]:
                    min = pivo
            arr[i], arr[min] = arr[min], arr[i]
    arr.pop(0)
    arr.pop(-1)
    return sum(arr)

if __name__ == "__main__":
    arr = [6, 2, 1, 8, 10]
    print(sum_array(arr))