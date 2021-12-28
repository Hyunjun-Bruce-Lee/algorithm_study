### https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(sample_text):
    if len(sample_text) == 1:
        return 1
    anss = list()
    for step in range(1,len(sample_text)//2+1):
        count, start_idx = 1, 0
        ans = str()
        for i in range(step,len(sample_text),step):
            if sample_text[start_idx:i] == sample_text[i:i+step]:
                count += 1
            else:
                if count == 1:
                    ans += sample_text[start_idx:i]
                else:
                    ans += str(count) + sample_text[start_idx:i]
                count = 1
            start_idx = i
        if count != 1:
            ans += str(count) + sample_text[i:i+step]
        else:
            ans += sample_text[i:i+step]
        anss.append(len(ans))
    return min(anss)
