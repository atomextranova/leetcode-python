def get_inorder(self, root):
    dummy = TreeNode(0)
    dummy.right = root
    # Dummy is important
    stack = [dummy]
    inorder_stack = []
    while stack:
        node = stack.pop()
        if node.right:
            node = node.right
            while node:
                stack.append(node)
                node = node.left
        if stack:
            inorder_stack.append(stack[-1].val)
    return inorder_stack