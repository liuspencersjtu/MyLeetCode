def closestValue(self, root, target):
        # write your code here
        res = root.val
        closest = abs(target-root.val)
        while root:
            if abs(target-root.val)<closest:
                closest = abs(target-root.val)
                res = root.val
            if root.val>target:
                root = root.left
            else:
                root = root.right
        return res
