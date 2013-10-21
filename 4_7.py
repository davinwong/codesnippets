class node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


def is_tree_subset(big_tree, small_tree):
    if big_tree.data == small_tree.data:
        match_tree(big_tree, small_tree)
        #return
    else:
        is_tree_subset(big_tree.left, small_tree)
        is_tree_subset(big_tree.right, small_tree)


def match_tree(big_tree, small_tree):
    # if big_tree == None or small_tree == None:
        # return
    if small_tree.data != big_tree.data:
        return False
    
    if small_tree.left and small_tree.right:
        return match_tree(small_tree.left, big_tree.left) and match_tree(small_tree.right, big_tree.right)
    elif small_tree.left:
        return match_tree(small_tree.left, big_tree.left)
    elif small_tree.right:
        return match_tree(small_tree.right, big_tree.right)
    else:
        return True


def main():

    tree1 = node(1,
        node(2,
            node(4),
            node(5)
        ), 
        node(3,
            node(6),
            node(7)
        )
    )

    tree2 = node(1,
        node(2,
            node(4),
            node(5)
        ), 
        node(3,
            node(6),
            node(7)
        )
    )

    print match_tree(tree1, tree2)

main()