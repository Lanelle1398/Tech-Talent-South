from itertools import product

A = (1, 2)
B = (3, 4)
# using the product() method , return the cartesian product
A=map(int, input().split())
B=map(int, input().split())
print(*product(A, B))
