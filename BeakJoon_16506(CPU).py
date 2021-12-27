### https://www.acmicpc.net/problem/16506

opcode = {
    'ADD' : '0000','SUB' : '0001',
    'MOV' : '0010','AND' : '0011',
    'OR' : '0100','NOT' : '0101',
    'MULT' : '0110','LSFTL' : '0111',
    'LSFTR' : '1000','ASFTR' : '1001',
    'RL' : '1010','RR' : '1011'}


n = int(input())
x_list = list()
for i in range(n):
    x_list.append(input().split())
    
for x_in in x_list:
    if 'C' in x_in[0]:
        head = opcode[x_in[0][:-1]] + '1'
        d_3rd = format(int(x_in[3]), 'b').zfill(4)
    else:
        head = opcode[x_in[0]] + '0'
        d_3rd = format(int(x_in[3]), 'b').zfill(3) + '0'
    d_1st = format(int(x_in[1]), 'b').zfill(3)
    d_2nd = format(int(x_in[2]),'b').zfill(3)
    print(head + '0' + d_1st + d_2nd + d_3rd)
