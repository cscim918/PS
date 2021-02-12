n = int(input())
s = [[0] * 3 for i in range(26)]
def preorder(a):
    print(a, end='')
    if s[ord(a)-65][1] != ".":
        preorder(s[ord(a)-65][1])
    if s[ord(a)-65][2] != ".":
        preorder(s[ord(a)-65][2])
def inorder(a):
    if s[ord(a)-65][1] != ".":
        inorder(s[ord(a)-65][1])
    print(a, end='')
    if s[ord(a)-65][2] != ".":
        inorder(s[ord(a)-65][2])
def postorder(a):
    if s[ord(a)-65][1] != ".":
        postorder(s[ord(a)-65][1])
    if s[ord(a)-65][2] != ".":
        postorder(s[ord(a)-65][2])
    print(a, end='')

for i in range(n):
    root, left, right = map(str, input().split())
    ro = ord(root) - 65
    s[ro][0], s[ro][1], s[ro][2] = root, left, right

preorder("A")
print()
inorder("A")
print()
postorder("A")