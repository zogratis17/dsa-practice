class Node:
    def __init__(self, v):
        self.v = v
        self.l = None
        self.r = None

n = int(input().strip())
nodes = {}
children = set()

for _ in range(n):
    a, b, c = input().split()
    if a not in nodes:
        nodes[a] = Node(int(a))
    x = nodes[a]
    if b != "None":
        if b not in nodes:
            nodes[b] = Node(int(b))
        x.l = nodes[b]
        children.add(b)
    if c != "None":
        if c not in nodes:
            nodes[c] = Node(int(c))
        x.r = nodes[c]
        children.add(c)

root_key = (set(nodes.keys()) - children).pop()
root = nodes[root_key]

out = []
stack = []
cur = root
while cur or stack:
    while cur:
        stack.append(cur)
        cur = cur.l
    cur = stack.pop()
    if cur.v % 2 == 0:
        out.append(cur.v)
    cur = cur.r

print(*out)
