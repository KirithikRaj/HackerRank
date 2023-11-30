# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def num(nam):
    if nam in phonebook:
        print(nam+"="+phonebook[nam])
    else:
        print("Not found")

n = int(input().strip())
phonebook = {}
for i in range(n):
    name, number = input().split()
    phonebook[name] = number
for line in sys.stdin:
    num(line.strip())
