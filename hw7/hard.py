# Prompt to ChatGPT: "Provide BST insert, delete_node, pretty printer, demo of deletions, and essay docstring."
# File: hard.py

"""
Essay: Deleting a Node from a Binary Search Tree

Deleting a node involves three cases:
1) Leaf node: remove it (set parent's pointer to None).
2) One child: replace node with its single child.
3) Two children: replace node's value with in-order successor (min in right subtree)
   then delete that successor node.

Edge cases:
- Deleting the root needs returning the new root.
- Unbalanced trees degrade to O(n).
- Handling duplicates depends on convention (this code places equals to the right).

Time Complexity: O(h) where h is tree height (O(log n) average, O(n) worst-case).
"""

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

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete_node(root, value):
    if root is None:
        return None
    if value < root.value:
        root.left = delete_node(root.left, value)
    elif value > root.value:
        root.right = delete_node(root.right, value)
    else:
        # no children
        if root.left is None and root.right is None:
            return None
        # one child
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        # two children: replace with in-order successor
        succ = find_min(root.right)
        root.value = succ.value
        root.right = delete_node(root.right, succ.value)
    return root

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
    # Demo: build tree, print, delete nodes with different cases, and print after each deletion
    values = [50, 30, 70, 20, 40, 60, 80, 65]
    root = None
    for v in values:
        root = insert(root, v)

    print("Original BST (hard.py) — pretty view:")
    print_tree_pretty(root)

    # Delete a leaf node (20)
    root = delete_node(root, 20)
    print("\nAfter deleting leaf 20:")
    print_tree_pretty(root)

    # Delete a leaf node (65)
    root = delete_node(root, 65)
    print("\nAfter deleting 65 (leaf):")
    print_tree_pretty(root)

    # Delete a node with two children (50)
    root = delete_node(root, 50)
    print("\nAfter deleting 50 (node with two children):")
    print_tree_pretty(root)