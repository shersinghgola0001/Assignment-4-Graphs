#Q3. Count the number of nodes at given level in a tree using BFS.
from collections import deque
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def count_nodes_at_level(root, target_level):
    if not root:
        return 0
    queue = deque([(root, 0)])  
    count = 0
    while queue:
        node, level = queue.popleft()
        if level == target_level:
            count += 1
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    return count
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

target_level = 2  
count = count_nodes_at_level(root, target_level)
print(f"Number of nodes at level {target_level}: {count}")
