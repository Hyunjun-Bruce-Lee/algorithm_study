### https://programmers.co.kr/learn/courses/30/lessons/42746

# 1차 풀이
solution = lambda test : ''.join(sorted(sorted(map(str,test),reverse=True), key = lambda x: str(x)[0], reverse = True))


# 2차 풀이
solution = lambda test : ''.join(sorted(map(str,test), key = lambda x: x*3, reverse = True))


# 3차 풀이
solution = lambda test : str(int(''.join(sorted(map(str,test), key = lambda x: x*3, reverse = True))))
