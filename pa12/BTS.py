n = int(input())
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
        self.depth = 0
class BTS:
    def __init__(self):
        self.root = None
    def insert(self, val, d):
        self.root = self._insert(self.root, val, d)
        return self.root is not None
    def _insert(self, node, val, d):
        if node is None:
            t = TreeNode(val)
            t.depth = d
            return t
        if val < node.val:
            d+=1
            node.left = self._insert(node.left, val, d)
        elif val > node.val:
            d+=1
            node.right = self._insert(node.right, val, d)
        else:
            return node
        return node
    def delete(self, val):
        self.root = self._delete(self.root, val)
    def _delete(self, node, val):
        if node is None:
            return None
        if val < node.val:
            node.left = self._delete(node.left, val)
            return node
        elif val > node.val:
            node.right = self._delete(node.right, val)
            return node
        else:
            if node.right == None and node.left == None:
                return None
            elif node.right is None:
                node.val = BTS._get_max_val(node.left)
                node.left = self._delete(node.left, node.val)
                return node
            else:
                node.val = BTS._get_min_val(node.right)
                node.right = self._delete(node.right, node.val)
                return node
    @classmethod
    def _get_min_val(cls, node):
        min_val = node.val
        while node.left:
            min_val = node.left.val
            node = node.left
        return min_val
    @classmethod
    def _get_max_val(cls, node):
        max_val = node.val
        while node.right:
            max_val = node.right.val
            node = node.right
        return max_val
    def min_depth(self, node):
        if node:
            self.min_depth(node.left)
            node.depth -= 1
            self.min_depth(node.right)
    def leaf(self, node):
        if node:
            self.leaf(node.left)
            if node.left is None and node.right is None:
                print(node.val, end=' ')
            self.leaf(node.right)
    def depth(self, node, num):
        if node:
            self.depth(node.left, num)
            if node.depth == num:
                print(node.val, end=' ')
            self.depth(node.right, num)
b = BTS()
for i in range(n):
    com = list(input().split())
    if com[0] == '+':
        d = 1
        b.insert(com[1], d)
    elif com[0] == '-':
        b.delete(com[1])
    elif com[0] == 'depth':
        b.depth(b.root, int(com[1]))
        print()
    else:
        b.leaf(b.root)
        print()