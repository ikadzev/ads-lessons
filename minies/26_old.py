class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def balanceBST(root: TreeNode) -> TreeNode:
    if not root:
        return TreeNode()
    balance_inner(root)
    return root


def balance_inner(root):  # 2
    if not root.right and not root.left:
        return [1, 0]
    r, rc = balance_inner(root.right) if root.right else [0, 0]
    l, lc = balance_inner(root.left) if root.left else [0, 0]

    c = r - l
    if abs(c) < 2:
        return [max(r, l) + 1, c]
    elif c == 2 and rc >= 0:
        temp_xb = [root, root.right.left]
        root = root.right
        temp_xb[0].right = temp_xb[1]
        root.left = temp_xb[0]
        return [r, rc - 1]
    elif c == -2 and lc >= 0:
        temp_xb = [root, root.left.right]
        root = root.left
        temp_xb[0].left = temp_xb[1]
        root.right = temp_xb[0]
        return [r, lc - 1]
    elif c == 2 and rc < 0:
        temp_xb = [root.right, root.right.left.right]
        root.right = root.right.left
        temp_xb[0].left = temp_xb[1]
        root.right.right = temp_xb[0]
        temp_xb = [root, root.right.left]
        root = root.right
        temp_xb[0].right = temp_xb[1]
        root.left = temp_xb[0]
        return [r, rc - 1]
    elif c == -2 and lc < 0:
        temp_xb = [root.left, root.left.right.left]
        root.left = root.left.right
        temp_xb[0].right = temp_xb[1]
        root.left.left = temp_xb[0]
        temp_xb = [root, root.left.right]
        root = root.left
        temp_xb[0].left = temp_xb[1]
        root.right = temp_xb[0]
        return [r, lc - 1]
    else:
        print('???')
        exit(1)


test = TreeNode(1, right=TreeNode(2, right=TreeNode(3, right=TreeNode(4))))
test = balanceBST(test)
print(test.val, test.right, test.left)
