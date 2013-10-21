class node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


def is_tree_subset(big_tree, small_tree):
    if big_tree is None:
        return False
    if big_tree.data == small_tree.data:
        if match_tree(big_tree, small_tree):
            return True

    # return true if either left or right contains subset
    return is_tree_subset(big_tree.left, small_tree) or is_tree_subset(big_tree.right, small_tree)


def match_tree(big_tree, small_tree):
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

    big_tree1 = node(1,
        node(2,
            node(4,
                node(8),
                node(9)
            ),
            node(5,
                node(10),
                node(11)
            )
        ), 
        node(3,
            node(6),
            node(7)
        )
    )

    big_tree2 = node(0,
        node(1,
            node(2,
                node(4,
                    node(8),
                    node(9)
                ),
                node(5,
                    node(10),
                    node(11)
                )
            ), 
            node(3,
                node(6),
                node(7)
            )
        )
    )

    big_tree3 = node(0,
        node(1,
            node(2,
                node(4,
                    node(8),
                    node(9)
                ),
                node(5,
                    node(10),
                    node(11)
                )
            ), 
            node(3,
                node(6),
                node(2000)
            )
        )
    )



    small_tree = node(1,
        node(2,
            node(4),
            node(5)
        ), 
        node(3,
            node(6),
            node(7)
        )
    )

    # true because big just has extra nodes
    print is_tree_subset(big_tree1, small_tree)

    # true because big just has extra root
    print is_tree_subset(big_tree2, small_tree)

    # false because 7 became 2000
    print is_tree_subset(big_tree3, small_tree)

main()