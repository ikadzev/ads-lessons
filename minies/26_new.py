class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def balance_bst(root: TreeNode) -> TreeNode:
    if not root:
        return root
    lst = to_list(root)
    root = to_bst(lst)
    return root


def to_list(root: TreeNode) -> list[int]:
    if not root.right and not root.left:
        return [root.val]
    lst = []
    lst.extend(to_list(root.left)) if root.left else None
    lst.append(root.val)
    lst.extend(to_list(root.right)) if root.right else None
    return lst


def to_bst(lst: list[int]) -> TreeNode:
    root = TreeNode(lst[len(lst) // 2])
    if len(lst) == 1:
        return root
    root.left = to_bst(lst[:len(lst) // 2])
    root.right = to_bst(lst[len(lst) // 2 + 1:]) if len(lst) > 2 else None
    return root


tree = TreeNode(1, right=TreeNode(2, right=TreeNode(3, right=TreeNode(4, right=TreeNode(5)))))
print(balance_bst(tree))