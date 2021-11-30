import sys
input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0]*(v+1)

for i in range(1, v+1):
    parent[i] = i

edges = []

for i in range(1, v+1):
    data = [0]+list(map(int, input().split()))
    for j in range(1, v+1):
        if data[j] == 1:
            edges.append((i, j))

for edge in edges:
    a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)


answer = "YES"

route = list(map(int, input().split()))
pre = parent[route[0]]

for i in range(1, len(route)):
    if pre != parent[route[i]]:
        answer = "NO"

print(answer)
