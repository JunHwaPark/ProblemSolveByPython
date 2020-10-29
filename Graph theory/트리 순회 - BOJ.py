n = int(input())
tree = dict()
for _ in range(n):
    parent, left, right = input().split()
    tree[parent] = [left, right]


def preorder(node):
    print(node, end='')
    if tree[node][0] != '.':
        preorder(tree[node][0])
    if tree[node][1] != '.':
        preorder(tree[node][1])


def inorder(node):
    if tree[node][0] != '.':
        inorder(tree[node][0])
    print(node, end='')
    if tree[node][1] != '.':
        inorder(tree[node][1])


def postorder(node):
    if tree[node][0] != '.':
        postorder(tree[node][0])
    if tree[node][1] != '.':
        postorder(tree[node][1])
    print(node, end='')


preorder('A')
print()
inorder('A')
print()
postorder('A')
print()