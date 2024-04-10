# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

N, M = map(int, input().split())
default = defaultdict(list)

for i in range(N):
    inp = input().rstrip()
    default[inp].append(i+1)
    
for i in range(M):
    inp = input().rstrip()
    
    if inp in default:
        print(' '.join(map(str, default[inp])))
    else:
        print('-1')

