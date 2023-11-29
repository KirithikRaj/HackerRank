if __name__ == '__main__':
    N = int(input())
    arr = []*N
    for i in range(N):
        op = str(input())
        command = list(op.split())
        if 'append' in op:
            arr.append(int(command[1]))
        elif 'insert' in op:
            arr.insert(int(command[1]), int(command[2]))
        elif 'print' in op:
            print(arr)
        elif 'remove' in op:
            arr.remove(int(command[1]))
        elif 'sort' in op:
            arr.sort()
        elif 'pop' in op:
            arr.pop()
        elif 'reverse' in op:
            arr.reverse()
