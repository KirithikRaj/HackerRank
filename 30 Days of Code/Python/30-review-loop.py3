# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input().strip())
for i in range(n):
    string = str(input().strip())
    even, odd = "", ""
    for j, v in enumerate(string):
        if j % 2:
            odd += v
        else:
            even += v
    print(even, odd)
