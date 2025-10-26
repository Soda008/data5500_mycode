# File: easy.py

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    """
    Insert value into BST. Returns the (possibly new) root.
    Time Complexity: O(log n) average, O(n) worst-case (unbalanced)
    """
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def _gather_levels(root):
    """Return list of levels; each level is list of nodes or None."""
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
    """
    Print a centered, layered ASCII representation of the tree.
    Uses level-order spacing to approximate a balanced layout suitable for terminals.
    """
    levels = _gather_levels(root)
    if not levels:
        print("<empty tree>")
        return

    height = len(levels)
    max_width = 2 ** (height - 1)
    col_width = 4  # space per node slot

    for i, level in enumerate(levels):
        gap = max_width // (2 ** i)
        line_elems = []
        for node in level:
            if node is None:
                line_elems.append(" " * col_width)
            else:
                s = str(node.value)
                # center within slot
                line_elems.append(s.center(col_width))
        # join with spacing
        spacing = " " * (gap * col_width - col_width)
        print(spacing.join(line_elems).rstrip())
        # print connectors between this level and next (except after the last)
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
    # Demo: build a BST and print it using the prettier printer
    values = [50, 30, 70, 20, 40, 60, 80]
    root = None
    for v in values:
        root = insert(root, v)

    print("Binary Search Tree (easy.py)")
    print_tree_pretty(root)