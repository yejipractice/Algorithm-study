import sys
from types import resolve_bases
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


v = int(input())
e = int(input())

parent = [[0] * (v+1)]
for i in range(1, v+1):
    parent[i] = i

result = 0

for i in range(1, e+1):
    data = find_parent(parent, int(input()))
    if data == 0:
        break
    else:
        result += 1
        union_parent(parent, data, data-1)

print(result)

# 루트가 0이면 union 못하도록, 0이 아니면 루트-1과 union << 알고리즘 생각해내기,,
