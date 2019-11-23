def signal_generator(n):
    present_num = 1983
    mod_num = 2 ** 32
    for _ in range(n):
        yield present_num % 10000 + 1
        present_num = (present_num * 214013 + 2531011) % mod_num


def solution(k, n):
    ans = 0
    part_sum = 0
    part_list = []
    for s in signal_generator(n):
        part_list.append(s)
        part_sum += s
        while part_sum > k:
            part_sum -= part_list.pop(0)
        if part_sum == k:
            ans += 1
    return ans


print(solution(3578452, 5000000))