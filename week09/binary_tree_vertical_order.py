class Solution:
    # TC: O(NlogN + N) -> O(N), N = Number of nodes
    # We have to check every node in the binary tree
    # every single time which constitutes for O(N)
    # complexity.
    # In addition, the sorting takes O(NlogN) time which
    # dominates the complexity. Hence, the time complexity
    # will be O(NlogN)

    # SC: O(N), N = Number of nodes
    # Because in the worst case scenario all the nodes at a single
    # time will be in the queue. That will drive the space
    # complexity to O(N)
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        node_map = collections.defaultdict(list)
        node_queue = deque([(root, 0)])

        while node_queue:
            node, column = node_queue.popleft()

            if node:
                node_map[column].append(node.val)
                node_queue.append((node.left, column - 1))
                node_queue.append((node.right, column + 1))
        return [node_map[x] for x in sorted(node_map.keys())]
