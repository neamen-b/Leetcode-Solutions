def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        def recurse(node, parent, pos):
            nonlocal val
            if node is None:
                if pos == 1:
                    # print("here")
                    parent.right = TreeNode(val)
                else:
                    # print("here")
                    parent.left = TreeNode(val)
                return None
            # print(node.val, val)
            if node.val < val:
                recurse(node.right, node, 1)
            elif node.val > val:
                recurse(node.left, node, 0)
            else:
                pass
        recurse(root, None, 0)
        return root