class ListNode:

    def __init__(self, val, next):
        self.val = val
        self.next = next

def do_intersect(head1, head2):

    node1 = head1
    node2 = head2

    if not node1 or not node2:
        return None

    node1_set = set()
    while node1:
        node1_set.add(node1)
        node1 = node1.next

    while node2:
        if node2 in node1_set:
            return node2

        node2 = node2.next


    return None


head1 = ListNode(0, None)
head1.next = ListNode(1, None)
target = head1.next.next = ListNode(2, None)
target.next = ListNode(3, None)
head2 = ListNode(10, target)

print(do_intersect(head1, head2).val)
