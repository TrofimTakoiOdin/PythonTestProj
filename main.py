def chunked(lst, n):
    k = []
    for i in range(0, len(lst), n):
        k.append(lst[i:i+n])
    return k


lst = input().split()
n = int(input())
print(chunked(lst, n))
