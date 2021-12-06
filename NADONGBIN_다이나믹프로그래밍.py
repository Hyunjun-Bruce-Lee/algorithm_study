# https://www.youtube.com/watch?v=5Lu34WIx2Us&t=1618s

#### 1
foods = [1,3,1,1,10,1,5]

memo = [0]*100
memo[0] = foods[0]
memo[1] = max(foods[0],foods[1])

for i in range(2,len(foods)):
    memo[i] = max(memo[i-1], memo[i-2] + foods[i])

print(memo)


#### 2
num = 26 

memo = [0]*100

for i in range(2,num+1):
    memo[i] = memo[i-1] + 1
    if i%2 == 0:
        memo[i] = min(memo[i], memo[i//2] + 1)
    if i%3 == 0:
        memo[i] = min(memo[i], memo[i//3] + 1)
    if i%5 == 0:
        memo[i] = min(memo[i], memo[i//5] + 1)

memo[num]


#### 3

n, m = 3, 17
coins = [2,3,5]

memo = [10001]*(m+1)

memo[0] = 0
for i in range(n):
    for j in range(coins[i], m+1):
        if memo[j-coins[i]] != 10001:
            memo[j] = min(memo[j], memo[j-coins[i]]+1)

if memo[m] == 10001:
    print(-1)
else:
    print(memo[m])
