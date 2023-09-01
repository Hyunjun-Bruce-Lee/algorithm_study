### https://school.programmers.co.kr/learn/courses/30/lessons/172928

def solution(park, routes):
    bord = [list(i) for i in park]
    park_string = ''.join(park)
    bord_size = (len(park), len(park[0]))
    loc_x, loc_y = divmod(park_string.index('S'),bord_size[1])

    move_dict = {'N':(-1,0),'S':(1,0),'W':(0,-1),'E':(0,1)}

    for route in routes:
        direction, step = route.split(' ')
        move_x, move_y = move_dict[direction]
        temp_x, temp_y, flag = loc_x, loc_y, True
        for _ in range(int(step)):
            new_x, new_y = temp_x + move_x, temp_y + move_y
            if (new_x < 0) | (new_y < 0):
                flag = False
                break
            elif (new_x > bord_size[0]-1) | (new_y > bord_size[1]-1):
                flag = False
                break

            if bord[new_x][new_y] == 'X':
                flag = False
                break
            else:
                temp_x, temp_y = new_x, new_y

        if flag:
            loc_x, loc_y = temp_x, temp_y
            
    return [loc_x,loc_y]