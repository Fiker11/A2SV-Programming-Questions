if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr1 = sorted(list(arr), reverse=True)
    for i in range(n):
        if arr1[i]>arr1[i+1]:
            print(arr1[i+1])
            break
             