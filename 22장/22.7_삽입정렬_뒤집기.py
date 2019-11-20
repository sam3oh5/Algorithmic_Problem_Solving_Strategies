import random


# 코드 22.3
# 트립의 한 노드를 저장한다.
class Node:
    def __init__(self, key: int):
        self.key = key # 노드에 저장된 원소
        self.priority = random.randint(0, 50000) # 이 노드의 우선순위, 난수로 우선순위 생성
        self.size = 1 # 이 노드를 루트로 하는 서브트리의 크기
        # 두 자식노드, None으로 초기화
        self.left = None
        self.right = None

    def set_left(self, new_left):
        self.left = new_left
        self.calc_size()

    def set_right(self, new_right):
        self.right = new_right
        self.calc_size()

    # size를 갱신한다.
    def calc_size(self):
        self.size = 1
        if self.left:
            self.size += self.left.size
        if self.right:
            self.size += self.right.size


#코드 22.4
# root를 루트로 하는 트립을 key 미만의 값과 이상의 값을 갖는
# 두 개의 트립으로 분리한다.
def split(root: Node, key: int) -> (Node, Node):
    if not root:
        return (None, None)
    # 루트가 key 미만이면 오른쪽 서브트리를 쪼갠다.
    if root.key < key:
        rs = split(root.right, key)
        root.set_right(rs[0])
        return (root, rs[1])
    # 루트가 key 이상이면 왼쪽 서브트리를 쪼갠다.
    ls = split(root.left, key)
    root.set_left(ls[1])
    return (ls[0], root)


# 코드22.4
# root를 투르로 하는 트립에서 새 노드 node를 삽인한 뒤 결과 트립의
# 루트를 반환한다.
def insert(root: Node, node: Node) -> Node:
    if not root:
        return node
    # node가 루트를 대체해야 한다. 해당 서브트리를 반으로 잘라
    # 각각 자손으로 한다.
    if node.priority > root.priority:
        splitted = split(root, node.key)
        node.set_left(splitted[0])
        node.set_right(splitted[1])
        return node
    elif node.key < root.key:
        root.set_left(insert(root.left, node))
    else:
        root.set_right(insert(root.right, node))
    return root


# a와 b가 두 개의 트립이고, max(a) < min(b)일 때 이 둘을 합친다.
def merge(a: Node, b: Node) -> Node:
    if not a:
        return b
    if not b:
        return a
    if a.priority < b.priority:
        b.set_left(merge(a, b.left))
        return b
    a.set_right(merge(a.right, b))
    return a

def erase(root: Node, key: int) -> Node:
    if not root:
        return root
    # key를 가지는 node를 지우고, 해당 node의 양 서브트리를 합친 뒤 반환한다.
    if root.key == key:
        ret = merge(root.left, root.right)
        return ret
    if root.key > key:
        root.set_left(erase(root.left, key))
    else:
        root.set_right(erase(root.right, key))
    return root


# 코드 22.6
# root를 루트로 하는 트리 중에서 k번째 원소를 반환한다.
def kth(root: Node, k: int) -> Node:
    # 왼쪽 서브트리의 크기를 우선 계산한다.
    left_size = 0
    if root.left:
        left_size = root.left.size
    if k <= left_size:
        return kth(root.left, k)
    if k == left_size + 1:
        return root
    return kth(root.right, k - left_size - 1)


# 코드 22.7
# key보다 작은 키값의 수를 반환한다.
def count_less_than(root: Node, key: int) -> int:
    if not root:
        return 0
    if root.key >= key:
        return count_less_than(root.left, key)
    ls = root.left.size if root.left else 0
    return ls + 1 + count_less_than(root.right, key)


def solve_with_list(shifted) -> list:
    A = []
    n_list = [i+1 for i in range(len(shifted))]

    for i in range(len(shifted)-1, -1, -1):
        n = n_list.pop(len(n_list) - shifted[i] - 1)
        A = [n] + A
    return A


def solve_with_binary_tree(shifted) -> list:
    # 1 - N까지의 숫자를 모두 저장하는 트립을 만든다.
    candidates = None
    for i in range(len(shifted)):
        candidates = insert(candidates, Node(i+1))
    A = []
    # 뒤에서부터 A[]를 채워나간다.
    for i in range(len(shifted)-1, -1, -1):
        # 후보 중 이 수보다 큰 수가 larger개 있다.
        larger = shifted[i]
        k = kth(candidates, i + 1 - larger)
        A = [k.key] + A
        candidates = erase(candidates, k.key)
    return A

shifted = [0, 1, 1, 2, 3]
print(solve_with_list(shifted))
print(solve_with_binary_tree(shifted))