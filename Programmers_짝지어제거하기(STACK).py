#### https://programmers.co.kr/learn/courses/30/lessons/12973
## 최초 풀이 시간초과
def solution(sample):
    sample = list(sample)
    while sample:
        re_idx = list()
        for i in range(len(sample)-1):
            if sample[i] == sample[i+1]:
                re_idx.extend([i,i+1])

        if re_idx == []:
            break

        count = 0
        for j in re_idx:
            j -= count
            del sample[j]
            count += 1
    return 1 if len(sample) == 0 else 0
  
  ## Stack을 이용한 풀이
  def solution(sample):
    stack = list()
    for i in sample:
        if not stack:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    return 1 if not stack else 0
