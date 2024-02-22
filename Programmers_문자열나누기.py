### https://school.programmers.co.kr/learn/courses/30/lessons/140108

def solution(s):
   ans = 0
   a,b = 0,0
   for i in s:
       if a==b:
           ans+=1
           j=i
       if j==i:
           a+=1
       else:
           b+=1
   return ans