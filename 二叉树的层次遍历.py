"""
    3
   / \
  9  20
    /  \
   15   7
[
  [3],
  [9,20],
  [15,7]
]
"""

class Solution:
    def levelOrder(self, root):

        if not root:
            return []
        result = []
        queue = [root]
        while queue:

            layer_result  = []
            next_queue = []
            for node in queue:
                layer_result.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            result.append(layer_result)
            queue = next_queue
        return result

