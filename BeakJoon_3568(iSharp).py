### https://www.acmicpc.net/problem/3568


temp = input().replace(',','').replace(';','').split()

for i in range(1,len(temp)):
    count,alpha_list = 0, list()
    for j in list(temp[i]):
        if j.isalpha():
            alpha_list.append(count)
        count += 1
    print(temp[0] + ''.join(reversed(temp[i][max(alpha_list)+1:])).replace('][','[]') + ' ' + temp[i][:max(alpha_list)+1] + ';')
