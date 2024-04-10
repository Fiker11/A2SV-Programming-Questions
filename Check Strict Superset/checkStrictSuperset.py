# Enter your code here. Read input from STDIN. Print output to STDOUT
main_set = set(input().split())
N = int(input())
total_set = set()

for i in range(N):
    total_set = total_set.union(set(input().split()))

print(len(total_set) == len(main_set.intersection(total_set)))