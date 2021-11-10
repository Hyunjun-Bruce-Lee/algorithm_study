directions = {
    0: [-1,0],
    3: [0,-1],
    2: [1,0],
    1: [0,1]
}

def move(location, bord, count):
    x,y,d = location
    bord[x][y] = 2
    for _ in range(4):
        d = (d+3)%4
        mx, my = directions[d]
        if x+mx not in range(len(bord)) and y+my not in range(len(bord[0])):
            continue
        if bord[x+mx][y+my] == 1 or bord[x+mx][y+my] == 2:
            continue
        else:
            x += mx
            y += my
            count += 1
            break
    return [x,y,d], bord, count

def move_till_end(location, bord, count):
    while True:
        previous_loc = location.copy()
        location, bord, count = move(location, bord, count)
        if previous_loc == location:
            break
    return location, bord, count

def move_back(location):
    x,y,d = location
    back_loc = (d + 2)%4
    mx,my = directions[back_loc]
    if bord[x+mx][y+my] != 1:
        x += mx
        y += my
    return [x,y,d]

n,m = list(map(int, input().split()))
location = list(map(int, input().split()))

bord = list()
for i in range(n):
    line = list(map(int, input().split()))
    bord.append(line)

count = 1
while True:
    location, bord, count = move_till_end(location, bord, count)
    previous_loc = location.copy()
    location = move_back(location)
    if previous_loc == location:
        break

count
