class node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def find_ancestor(self, node1, node2):
        # if both in left, move left
        if self.left.in_tree(node1) and self.left.in_tree(node2):
            # print "both in left"
            # need to continuously return the node value here to prevent None`
            return self.left.find_ancestor(node1, node2)
        elif self.right.in_tree(node1) and self.right.in_tree(node2):
            # print "both in right"
            return self.right.find_ancestor(node1, node2)
        else:
            # print "1 in each"
            return self

    def in_tree(self, n):
        if self is n:
            return True
        elif self.left is None and self.right is None:
            return False
        return self.left.in_tree(n) or self.right.in_tree(n)

def main():
    tree = node(1,
            node(2,
                node(4),
                node(5)
            ), 
            node(3,
                node(6),
                node(7)
            )
        )

    # print tree.left.left

    print tree.find_ancestor(tree.left.left, tree.left.right)

main()
