# File: hard.py

# Essay:
# Deleting a Node from a Binary Search Tree in Python
# Deleting a node from a BST means removing the node while keeping the tree’s left < parent < right ordering.
# Deletion
#   - Leaf node
#       - Action: Remove it by setting the parent’s pointer to None.
#       - Why: No children to reconnect, so removal is straightforward.
#   - Node with one child
#       - Action: Replace the node with its single child by updating the parent’s pointer to point to that child.
#       - Why: The subtree rooted at the child preserves the BST ordering when spliced in place of the deleted node.
#   - Node with two children
#       - Action: Find the node’s in-order successor (the smallest node in its right subtree),
#           copy the successor’s value into the node to delete, then delete the successor node from the right subtree.
#       - Why: The successor is the next larger value, so copying it preserves ordering;
#           the successor will have at most one child, reducing the problem to a simpler case.
# Edge Cases and Special Circumstances
#   - Deleting the root
#       - You must return the new root after deletion because the root variable may change when the root is removed or replaced.
#   - Duplicates
#       - Decide a convention up front (e.g., place equal values on the right).
#           Follow that convention consistently in insert/search/delete so duplicate handling is predictable.
#   - Unbalanced trees
#       - Repeated insertions/deletions can make the tree skewed, turning O(log n) operations into O(n).
#           For predictable performance, use a self-balancing tree (AVL/Red‑Black) or rebalance periodically.
#   - Missing value or empty tree
#       - If the value isn’t found or the tree is empty, simply return the original root; do not raise errors.
#   - Parent pointer management and references
#       - If using recursion, return the updated subtree root from each call so parent links are correct;
#           if using iteration, carefully update parent child pointers.

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