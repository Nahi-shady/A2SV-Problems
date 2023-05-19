def insertionSort1(n, arr):
    value = arr[-1]
    index = n-1
    while arr[index-1] > value and index > 0:
        arr[index] = arr[index-1]
        index-=1
        print(' '.join(map(str,arr)))
    arr[index] = value
    print(' '.join(map(str,arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
