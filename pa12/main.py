n = int(input())

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.depth = 0

class Binary_Search_Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            self.root.depth = 1
        else:
            self.base = self.root
            dep = 1
            while True:
                if data == self.base.data:
                    break
                elif data > self.base.data:
                    if self.base.right is None:
                        self.base.right = Node(data)
                        self.base.right.depth = dep + 1
                        break
                    else:
                        self.base = self.base.right
                        dep += 1
                else:
                    if self.base.left is None:
                        self.base.left = Node(data)
                        self.base.left.depth = dep+1
                        break
                    else:
                        self.base = self.base.left
                        dep += 1

    def remove(self, data):
        self.searched = False
        self.cur_node = self.root
        self.parent = self.root
        while self.cur_node:
            if self.cur_node.data == data:
                self.searched = True
                break
            elif self.cur_node.data > data:
                self.parent = self.cur_node
                self.cur_node = self.cur_node.left
            else:
                self.parent = self.cur_node
                self.cur_node = self.cur_node.right
        if self.searched:
            # 1.자식 노드가 없는 경우
            if self.cur_node.left is None and self.cur_node.right is None:
                if self.cur_node.depth == 1:
                    self.root = None
                else:
                    if self.parent.data > self.cur_node.data:
                        self.parent.left = None
                        self.cur_node = None
                    else:
                        self.parent.right = None
                        self.cur_node = None
            # 2.자식 노드가 있는 경우
            else:
                # [1] 오른쪽 자식 노드가 없는 경우
                self.d_node = self.cur_node
                if self.cur_node.right is None:
                    self.parent = self.cur_node
                    self.cur_node = self.cur_node.left
                    while True:
                        if self.cur_node.right is not None:
                            self.parent = self.cur_node
                            self.cur_node = self.cur_node.right
                        else:
                            if self.parent == self.d_node:
                                self.parent.left = self.cur_node.left
                                self.d_node.data = self.cur_node.data
                                self.minus_dept(self.parent.left)
                            else:
                                self.parent.right = self.cur_node.left
                                self.d_node.data = self.cur_node.data
                                self.minus_dept(self.parent.right)
                            break
                # [2] 오른쪽 자식 노드가 있는 경우
                else:
                    self.parent = self.cur_node
                    self.cur_node = self.cur_node.right
                    while True:
                        if self.cur_node.left is not None:
                            self.parent = self.cur_node
                            self.cur_node = self.cur_node.left
                        else:
                            if self.parent == self.d_node:
                                self.parent.right = self.cur_node.right
                                self.d_node.data = self.cur_node.data
                                self.minus_dept(self.parent.right)
                            else:
                                self.parent.left = self.cur_node.right
                                self.d_node.data = self.cur_node.data
                                self.minus_dept(self.parent.left)
                            break
        else:
            pass

    def minus_dept(self, node):
        if not node:
            return
        node.depth -= 1
        self.minus_dept(node.left)
        self.minus_dept(node.right)

    def depth(self, node, num):
        if not node:
            return
        if node.depth == num:
            print(node.data, end=' ')
        self.depth(node.left, num)
        self.depth(node.right, num)

    # 중위 순회
    def in_order_traverse(self, node):
        if not node:
            return
        self.in_order_traverse(node.left)
        if node.left is None and node.right is None:
            print(node.data, end=' ')
        self.in_order_traverse(node.right)

b = Binary_Search_Tree()

for i in range(n):
    command = list(input().split())
    if command[0] == '+':
        b.insert(command[1])
    elif command[0] == '-':
        b.remove(command[1])
    elif command[0] == 'depth':
        b.depth(b.root, int(command[1]))
        print()
    else:
        b.in_order_traverse(b.root)
        print()
