### https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(n,stages):
    result = {i:0 for i in range(1,n+1)}
    for stage in range(1,n+1):
        on_stage_cnt = sum(map(lambda x: True if x >= stage else False, stages))
        failed_cnt = sum(map(lambda x: True if x == stage else False, stages))
        if on_stage_cnt == 0:
            continue
        else:   
            result[stage] += (failed_cnt/on_stage_cnt)

    result = sorted(result.items(), key = lambda x: x[1], reverse = True)
    return [i[0] for i in result]


### 위 시간초과.
### 아래 시간복잡도 감소

def solution(n, stages):
    result = {i: 0 for i in range(1, n + 1)}
    on_stage_cnt = len(stages)

    for stage in stages:
        if stage <= n:
            result[stage] += 1

    failure_rates = []
    for stage in range(1, n + 1):
        if on_stage_cnt == 0:
            failure_rates.append((stage, 0))
        else:
            failure_rate = result[stage] / on_stage_cnt
            failure_rates.append((stage, failure_rate))
            on_stage_cnt -= result[stage]

    failure_rates = sorted(failure_rates, key=lambda x: x[1], reverse=True)
    return [i[0] for i in failure_rates]
