class ListNode:
    def __init__(self, data):
        self.val = data
        self.next = None


def list2linked(arr):
    """
    Turn list into linked list
    :param arr: list[int]
    :return: linked list node
    """
    root = ListNode(arr[0])
    temp = root
    for i in range(1, len(arr)):
        temp.next = ListNode(arr[i])
        temp = temp.next
    return root


def linked2list(root):
    """

    :param root:
    :return: list[int]
    """
    arr = []
    while root:
        arr.append(root.val)
        root = root.next
    return arr


def fun(root):
    """
    Find cycle
    :param root: linked list node
    :return: linked list node
    """
    pointer1 = root
    pointer2 = root

    while pointer2.next.next.next and pointer2.next.next.next.next:
        pointer1 = pointer1.next
        pointer2 = pointer2.next.next
        if pointer2 == pointer1:
            return pointer1

    return False


if __name__ == '__main__':
    root = list2linked([1, 2, 3, 4, 5, 6, 7])
    node6 = root

    for _ in range(6):
        node6 = node6.next

    node6.next = root.next
    node = fun(root)
    print(node.next.val)




