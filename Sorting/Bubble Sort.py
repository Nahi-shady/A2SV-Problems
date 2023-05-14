def countSwaps(a):
    
    index = len(a) - 1
    sorted_status = False
    count = 0
    
    while not sorted_status:
        sorted_status = True
        for i in range(index):
            if a[i] > a[i+1]:
                sorted_status = False
                a[i], a[i+1] = a[i+1], a[i]
                count += 1
        
    print(f'Array is sorted in {count} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')
