### https://www.acmicpc.net/problem/2309


from itertools import permutations

heights = list()
for _ in range(9):
    heights.append(int(input()))

target = sum(heights)-100

for i,j in list(permutations(heights, 2)):
    if i+j == target:
        heights.remove(i)
        heights.remove(j)
        break

heights.sort()

for i in heights:
    print(i)
