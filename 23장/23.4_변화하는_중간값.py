# 코드 23.1
# 정수를 담는 최대 힙 heap에 새 원소 new_value를 삽입한다.
def push_heap(heap: list, new_value: int) -> list:
    # 힙의 맨 끝에 new_value를 삽입한다.
    heap.append(new_value)
    idx = len(heap) - 1
    while idx > 0 and heap[(idx-1)//2] < heap[idx]:
        heap[(idx-1)//2], heap[idx] = heap[idx], heap[(idx-1)//2]
        idx = (idx - 1) // 2
    return heap


# 코드 23.2
# 정수를 담는 최대 힙 heap에서 heap[0]를 제거한다.
def pop_heap(heap: list) -> list:
    if len(heap) == 1:
        heap = []
    # 힙의 맨 끝에서 값을 가져와 루트에 덮어씌운다.
    else:
        heap[0] = heap.pop()
        here = 0
        while True:
            left = here*2+1
            right = here*2+2
            # 리프에 도달한 경우
            if left >= len(heap):
                break
            # heap[here]가 내려갈 위치를 찾는다.
            next = here
            if heap[next] < heap[left]:
                next = left
            if right < len(heap) and next < heap[right]:
                next = right
            if next == here:
                break
            heap[next], heap[here] = heap[here], heap[next]
            here = next
    return heap


# 코드 23.4 힙을 이용해 변화하는 중간 값 문제를 해결하는 함수의 구현
def running_median(n: int, rng) -> int:
    max_heap = []
    min_heap = []
    ret = 0
    # 반복문 불변식
    # 1. max_heap의 크기는 min_heap의 크기와 같거나 1 더 크다.
    # 2. max_heap root <= min_heap root
    for _ in range(n):
        # 우선 1번 불변식부터 만족시킨다.
        if len(max_heap) == len(min_heap):
            push_heap(max_heap, rng.next())
        else:
            push_heap(min_heap, -rng.next())
        if min_heap and max_heap and -min_heap[0] < max_heap[0]:
            a = max_heap[0]
            b = -min_heap[0]
            max_heap = pop_heap(max_heap)
            min_heap = pop_heap(min_heap)
            push_heap(max_heap, b)
            push_heap(min_heap, -a)
        ret = (ret + max_heap[0]) % 20090711
        print(ret)
    return ret


# 코드 23.5 변화하는 중간 값 문제의 입력 생성하기
class RNG():
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
        self.seed = 1983

    def next(self) -> int:
        ret = self.seed
        self.seed = (self.seed * self.a + self.b) % 20090711
        return ret


n = 10000
rng_key = [1273, 4936]
rng = RNG(*rng_key)
print(running_median(n, rng))