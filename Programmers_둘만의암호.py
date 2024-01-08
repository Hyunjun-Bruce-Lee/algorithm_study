### https://school.programmers.co.kr/learn/courses/30/lessons/155652

def solution(s, skip, index):
    ans = list()
    skip = [ord(i) - 97 for i in skip]
    for char in s:
          step, flag = index, (ord(char) - 97)
          while step != 0:
              flag += 1
              if flag >25:
                  flag -= 26
              if flag in skip:
                   continue
              else:
                   step -= 1
          ans.append(chr(flag + ord('a')))
    return ''.join(ans)