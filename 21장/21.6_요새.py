walls = [[21, 15, 20], [15, 15, 10], [13, 12, 5], [12, 12, 3], [19, 19, 2], [30, 24, 5], [32, 10, 7], [32, 9, 4]]
longest = 0


class TreeNode():
    def __init__(self):
        self.child = []


def sqrdist(w1, w2):
    return (w1[0] - w2[0])**2 + (w1[1] - w2[1])**2


def is_enclose(w1, w2):
    return (w1[2] < w2[2] and
            sqrdist(w1, w2) < (w2[2] - w1[2])**2)


def is_child(w_new, w_ori):
    if not is_enclose(w_new, w_ori):
        return False
    for w in walls[1:]:
        if (w != w_new and w != w_ori and
            is_enclose(w, w_ori) and is_enclose(w_new, w)):
            return False
    return True


def get_tree(wall):
    root = TreeNode()
    for w in walls[1:]:
        if is_child(w, wall):
            root.child.append(get_tree(w))
    return root


def height(root):
    global longest
    heights = []
    for child in root.child:
        heights.append(height(child))
    if not heights:
        return 0
    heights.sort()
    if len(heights) > 1:
        longest = max(longest, 2 + sum(heights[-2:]))
    return heights[-1] + 1

if __name__ == '__main__':
    root = get_tree(walls[0])
    h = height(root)
    print(max(longest, h))