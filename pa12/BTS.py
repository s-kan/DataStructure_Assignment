n = int(input())
# bts를 구성하는 노드 클래스 선언
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
        self.depth = 0
# bts 클래스 선언
class BTS:
    def __init__(self):
        self.root = None
    # insert 함수
    def insert(self, val, d):
        self.root = self._insert(self.root, val, d)
        return self.root is not None
    def _insert(self, node, val, d):
        # insert 할 자리를 찾으면(node == None) insert
        if node is None:
            t = TreeNode(val)
            t.depth = d
            return t
        # insert할 val 값이 현재 노드의 val 값보다 작으면 왼쪽 자식노드로 이동 (depth인 d값 1 추가)
        if val < node.val:
            d+=1
            node.left = self._insert(node.left, val, d)
        # insert할 val 값이 현재 노드의 val 값보다 크면 오른쪽 자식노드로 이동 (depth인 d값 1 추가)
        elif val > node.val:
            d+=1
            node.right = self._insert(node.right, val, d)
        # insert 값이 이미 있으면 insert 하지 않고 return
        else:
            return node
        return node
    # delete 함수
    def delete(self, val):
        self.root = self._delete(self.root, val)
    def _delete(self, node, val):
        # 삭제할 노드가 없으면 그냥 return None
        if node is None:
            return None
        # 삭제할 node의 val 값이 현재 node의 val 값보다 작으면 왼쪽 자식노드로 이동
        if val < node.val:
            node.left = self._delete(node.left, val)
            return node
        # 삭제할 node의 val 값이 현재 node의 val 값보다 크면 오른쪽 자식노드로 이동
        elif val > node.val:
            node.right = self._delete(node.right, val)
            return node
        # 삭제할 노드를 찾았을 경우
        else:
            # [1] 삭제할 노드의 자식 노드가 없는 경우(leaf)인 경우 그냥 삭제한다.
            if node.right == None and node.left == None:
                return None
            # [2] 삭제할 노드의 오른쪽 자식노드가 없는 경우 왼쪽 부트리 값중 가장 큰 값을 채운다.
            elif node.right is None:
                node.val = BTS._get_max_val(node.left)
                node.left = self._delete(node.left, node.val)
                return node
            # [3] 삭제할 노드의 왼쪽 자식노드가 없는 경우 오른쪽 부트리 값중 가장 작은 값을 채운다.
            else:
                node.val = BTS._get_min_val(node.right)
                node.right = self._delete(node.right, node.val)
                return node
    # 부트리 중 최소값을 리턴
    @classmethod
    def _get_min_val(cls, node):
        min_val = node.val
        while node.left:
            min_val = node.left.val
            node = node.left
        return min_val
    # 부트리 중 최대값을 리턴
    @classmethod
    def _get_max_val(cls, node):
        max_val = node.val
        while node.right:
            max_val = node.right.val
            node = node.right
        return max_val
    # 자신과 부트리의 depth를 1씩 빼주는 함수
    # delete 함수에 이용
    def min_depth(self, node):
        if node:
            self.min_depth(node.left)
            node.depth -= 1
            self.min_depth(node.right)
    # 순회 알고리즘을 이용하여 순회 중 노드의 오른쪽과 왼쪽 자식 노드가 None이면 출력
    def leaf(self, node):
        if node:
            self.leaf(node.left)
            if node.left is None and node.right is None:
                print(node.val, end=' ')
            self.leaf(node.right)
    # 순회 알고리즘을 이용하여 순회 중 depth 값이 주어진 값과 같으면 출력
    def depth(self, node, num):
        if node:
            self.depth(node.left, num)
            if node.depth == num:
                print(node.val, end=' ')
            self.depth(node.right, num)
b = BTS()
# 입력부
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