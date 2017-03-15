class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def inorder(root):
    if root is None:
        return ""

    res = ""
    res += inorder(root.left)
    res += "{} ".format(root.data)
    res += inorder(root.right)
    return res


def all_subtree(root):
    if root is None:
        return None

    res = [root.data]

    l = all_subtree(root.left)
    if l is not None:
        res += l
        res.append(l)

    r = all_subtree(root.right)
    if r is not None:
        res += r
        res.append(r)

    return res


def main():
    root = Node(8)
    root.left = Node(3)
    root.right = Node(10)

    print(inorder(root))
    print(all_subtree(root))


if __name__ == "__main__":
    main()
