class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def max_ancestor_diff (self, root):
    max_val = 0

    if root.left == None and root.right == None:
        return max_val

    if max_ancestor_diff(root.left > max_val):
        max_val = max_ancestor_diff(root.left > max_val)
    if max_ancestor_diff(root.right > max_val):
        max_val = max_ancestor_diff(root.right > max_val)

        