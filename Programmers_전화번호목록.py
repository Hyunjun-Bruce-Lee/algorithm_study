### https://programmers.co.kr/learn/courses/30/lessons/42577

## 효율성 실패 (시간초과)
def solution(phone):
    phone = sorted(phone, key = len)
    ans = True
    for i in range(len(phone)):
        for j in range(i+1,len(phone)):
            if phone[j][:len(phone[i])] == phone[i]:
                ans = False
                break
    return ans



## 해결
def solution(phone):
    phone = sorted(phone)
    ans = True
    for i in range(len(phone)-1):
        if phone[i] == phone[i+1][:len(phone[i])]:
            ans = False
            break
    return ans
