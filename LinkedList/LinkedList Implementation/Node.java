//Implementation of singly linked list

class Node {
    int data;
    Node next;

    public Node(int data) {
        this.data = data;
        next = null;
    }

    public void append(int data) {

        Node n = this;
        while(n.next != null) {
            n = n.next;
        }
        n.next = new Node(data);
    }

    public void removeAt(int index) {
        int i = 0;
        Node prev = this;
        while(i + 1 < index) {
            prev = prev.next;
        }

        prev.next = prev.next.next.next;
    }
}
