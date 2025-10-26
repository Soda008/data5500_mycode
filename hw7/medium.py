# File: medium.py

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def search(root, target):
    """
    Search for target in BST. Returns True if found, False otherwise.
    Time Complexity: O(log n) average, O(n) worst-case (unbalanced)
    """
    if root is None:
        return False
    if root.value == target:
        return True
    if target < root.value:
        return search(root.left, target)
    return search(root.right, target)

def _gather_levels(root):
    if not root:
        return []
    levels = []
    current = [root]
    while any(n is not None for n in current):
        levels.append(current)
        next_level = []
        for n in current:
            if n is None:
                next_level.extend([None, None])
            else:
                next_level.append(n.left)
                next_level.append(n.right)
        current = next_level
    return levels

def print_tree_pretty(root):
    if root is None:
        print("<empty tree>")
        return
    levels = _gather_levels(root)
    height = len(levels)
    max_width = 2 ** (height - 1)
    col_width = 4
    for i, level in enumerate(levels):
        gap = max_width // (2 ** i)
        line_elems = []
        for node in level:
            if node is None:
                line_elems.append(" " * col_width)
            else:
                line_elems.append(str(node.value).center(col_width))
        spacing = " " * (gap * col_width - col_width)
        print(spacing.join(line_elems).rstrip())
        if i < height - 1:
            conn_line = []
            for node in level:
                if node is None:
                    conn_line.append(" " * col_width)
                else:
                    left_conn = "/" if node.left else " "
                    right_conn = "\\" if node.right else " "
                    conn_line.append((left_conn + " " * (col_width - 2) + right_conn))
            print(spacing.join(conn_line).rstrip())

if __name__ == "__main__":
    # Build tree for demonstration
    values = [50, 30, 70, 20, 40, 60, 80]
    root = None
    for v in values:
        root = insert(root, v)

    print("Binary Search Tree (medium.py) — pretty view:")
    print_tree_pretty(root)

    # Demo searches
    tests = [60, 25, 80, 100]
    for t in tests:
        print(f"Searching for {t}: {search(root, t)}")