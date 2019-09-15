# 코드 23.1
# 정수를 담는 최대 힙 heap에 새 원소 new_value를 삽입한다.
def push_heap(heap: list, new_value: int) -> list:
    # 힙의 맨 끝에 new_value를 삽입한다.
    heap.append(new_value)
    idx = len(heap) - 1
    while idx > 0 and heap[(idx-1)/2] < heap[idx]:
        heap[(idx-1)/2], heap[idx] = heap[idx], heap[(idx-1)/2]
        idx = (idx - 1) // 2
    return heap

# 코드 23.2
# 정수를 담는 최대 힙 heap에서 heap[0]를 제거한다.
def pop_heap(heap: list) -> list:
    # 힙의 맨 끝에서 값을 가져와 루트에 덮어씌운다.
    heap[0] = heap.pop()
    int here = 0
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