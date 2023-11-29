if __name__ == '__main__':
    n = int(input())
    string = str(1)
    if n == 1:
        print(string)
    else:
        for i in range(2, n+1):
            string += str(i)
        print(string)
