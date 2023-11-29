if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n-1):
        for j in range(i + 1, n):
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
            else:
                j += 1
        i += 1
    max = arr[0]
    for i in range(n):
        if arr[i] != max:
            index = i
            break
    print(arr[index])
