# Enter your code here. Read input from STDIN. Print output to STDOUT
eng = int(input())
english = set(map(int, input().split()))
fre = int(input())
french = set(map(int, input().split()))

uni = english.union(french)
print(len(uni))