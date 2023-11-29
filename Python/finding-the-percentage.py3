if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_marks = student_marks[query_name]
    tot, m = 0, len(query_marks)
    for i in range(m):
        tot += query_marks[i]
    avg = float(tot/m)
    print('%.2f'% avg)
