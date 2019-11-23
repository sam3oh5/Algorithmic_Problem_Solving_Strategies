def print_postorder(preorder, inorder):
    if not preorder:
        return ''
    root = preorder[0]
    left_size = inorder.index(root)
    print_postorder(preorder[1:left_size + 1], inorder[:left_size])
    print_postorder(preorder[left_size + 1:], inorder[left_size + 1:])
    print(root, end=' ')


preorder = [27, 16, 9, 12, 54, 36, 72]
inorder = [9, 12, 16, 27, 36, 54, 72]
print_postorder(preorder, inorder)