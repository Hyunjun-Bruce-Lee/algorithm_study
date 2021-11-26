# https://www.acmicpc.net/problem/1991

class node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def pre_serch(node, temp = list()):
    temp.append(node.data)
    if node.left != '.':
        pre_serch(tree[node.left], temp)
    if node.right != '.':
        pre_serch(tree[node.right], temp)
    return temp


def mid_serch(node, temp = list()):
    if node.left != '.':
        mid_serch(tree[node.left], temp)
    temp.append(node.data)
    if node.right != '.':
        mid_serch(tree[node.right], temp)
    return temp


def aft_serch(node, temp = list()):
    if node.left != '.':
        aft_serch(tree[node.left], temp)
    if node.right != '.':
        aft_serch(tree[node.right], temp)
    temp.append(node.data)
    return temp

n = int(input())
tree = dict()
for i in range(n):
    data, left, right = input().split()
    tree[data] = node(data, left, right)


a = ''.join(pre_serch(tree['A']))
b = ''.join(mid_serch(tree['A']))
c = ''.join(aft_serch(tree['A']))

print(f"{a}\n{b}\n{c}")
