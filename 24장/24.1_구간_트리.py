import sys


MAX = sys.maxsize

# 코드 24.1 배열의 구간 최소 쿼리(RMQ) 문제를 해결하는 구간 트리의 초기화
# 배열의 구간 최소 쿼리를 해결하기 위한 구간 트리의 구현
class RMQ():
    def __init__(self, array: list):
        self.n = len(array) # 배열의 길이
        self.range_min = [0] * (self.n * 4)
        self.initialization(array, 0, self.n-1, 1)

    def initialization(self, array: list, left: int, right: int, node: int):
        """ node 노드가 array[left, right] 배열을 표현할 때
        node를 루트로 하는 서브트리를 초기화하고, 이 구간의 초소치를 반환한다."""
        if left == right:
            self.range_min[node] = array[left]
        else:
            mid: int = (left + right) // 2
            left_min: int = self.initialization(array, left, mid, node*2)
            right_min: int = self.initialization(array, mid+1, right, node*2+1)
            self.range_min[node] = min(left_min, right_min)
        return self.range_min[node]

    # 코드 24.2 RMQ 문제를 푸는 구간 트리에서 질의 연산의 구현
    def query(self, left: int, right: int, node: int=1, node_left: int=0,
              node_right=None):
        if not node_right:
            node_right = self.n - 1
        # 두 구간이 겹치지 않으면 아주 큰 값을 반환한다: 무시됨.
        if node >= len(self.range_min) or (right < node_left or left > node_right):
            return MAX
        # node가 표현하는 범위가 array[left, right]에 완전히 포함되는 경우
        if left <= node_left and right >= node_right:
            return self.range_min[node]
        # 양쪽 구간을 나눠서 푼 뒤 결과를 합친다.
        mid: int = (node_left + node_right) // 2
        return min(self.query(left, right, node*2, node_left, mid),
                   self.query(left, right, node*2+1, mid+1, node_right))

    # 코드 24.3 RMQ 문제를 푸는 구간 트리에서 갱신 연산의 구현
    def update(self, index: int, new_value: int, node: int=1, node_left: int=0,
               node_right=None):
        if not node_right:
            node_right = self.n - 1
        """ array[index]=new_value로 바뀌었을 때 node를 루트로 하는
        구간 트리를 갱신하고 노드가 표현하는 구간의 최소치를 반환한다."""
        # index가 노드가 표현하는 구간과 상관없는 경우엔 무시한다.
        if index < node_left or index > node_right:
            pass
        # 트리의 리프까지 내려온 경우
        elif node_left == node_right:
            self.range_min[node] = new_value
        else:
            mid: int = (left + right) // 2
            left_min: int = self.update(index, new_value, node*2, node_left, mid)
            right_min: int = self.update(index, new_value, node*2+1, mid+1, node_right)
            self.range_min[node] = min(left_min, right_min)
        return self.range_min[node]


def solution(heights, opens):
    min_heights = RMQ(heights)
    max_heights = RMQ([-h for h in heights])
    ans = []
    for left, right in opens:
        ans.append(-max_heights.query(left, right) - min_heights.query(left, right))
    return ans


heights = [3, 9, 5, 6, 10, 8, 7, 1, 2, 4]
opens = [[1, 6], [4, 7], [9, 9], [5, 8]]
print(solution(heights, opens))
