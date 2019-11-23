class Node:
    def __init__(self, value, next_):
        self.value = value
        self.next = next_


def solution(n, k):
    head = Node(1, None)
    present = head
    for i in range(2, n + 1):
        present.next = Node(i, None)
        present = present.next
        if i == n:
            present.next = head.next
            n -= 1
    while n > 2:
        pre = None
        for _ in range(k):
            pre = head
            head = head.next
        pre.next = head.next
        n -= 1
    return (head.next.value, head.next.next.value)


print(solution(40, 3))