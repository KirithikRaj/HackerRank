if __name__ == '__main__':
    nest_list = []
    for _ in range(int(input())):
        name, score = [], []
        name.append(str(input()))
        score = float(input())
        name.append(score)
        nest_list.append(name)
    for i in range(len(nest_list)-1):
        for j in range(i+1, len(nest_list)):
            if nest_list[i][1] > nest_list[j][1]:
                nest_list[i], nest_list[j] = nest_list[j], nest_list[i]
            else:
                j += 1
        i += 1
    min_value = min(list(map(lambda x: x[1], nest_list)))
    index = 0
    for i in range(len(nest_list)):
        if nest_list[i][1] > min_value:
            index = i
            break
    last = []
    last.append(nest_list[index][0])
    if index < len(nest_list)-1:
        if nest_list[index][1] == nest_list[index+1][1]:
            last.append(nest_list[index+1][0])
            last.sort()

    for i in range(len(last)):
        print(last[i])
