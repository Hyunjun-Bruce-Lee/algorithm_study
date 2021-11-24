# https://programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque(0 for i in range(bridge_length))
    trucks = deque(truck_weights)
    trucks.extend([0]*bridge_length)
    done_truck = list()
    
    turns = 0
    current_weight = 0
    while done_truck != truck_weights:
        temp_value = bridge.popleft()
        current_weight -= temp_value
        if (current_weight + trucks[0] <= weight):
            if temp_value != 0:
                done_truck.append(temp_value)
            single_truck = trucks.popleft()
            bridge.append(single_truck)
            current_weight += single_truck
            turns += 1
        else:
            if temp_value != 0:
                done_truck.append(temp_value)
            bridge.append(0)
            turns += 1
    return turns
