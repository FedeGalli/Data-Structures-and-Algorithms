public class MyQueue<T> {
    private static class QueueNode<T> {
        private T data;
        private QueueNode<T> next;

        public QueueNode(T data) {
            this.data = data;
            this.next = null;
        }

        public void append(T data) {

            QueueNode<T> n = this;

            while(n.next != null) {
                n = n.next;
            }

            n.next = new QueueNode<T>(data);

        }

        public void append(QueueNode<T> node) {

            QueueNode<T> n = this;

            if (n.data == null) {
                n = node;
                return;
            }


            while(n.next != null) {
                n = n.next;
            }

            n.next = node;

        }
    }

    private QueueNode<T> head;

    public MyQueue(T data) {
        this.head = new QueueNode<T>(data);
    }

    public void add(T data) {
        if (this.head.data == null)
            this.head.data = data;
        else {

            QueueNode<T> n = head;

            while (n.next != null) {
                n = n.next;
            }
            n.next = new QueueNode<T>(data);
        }
            
    }

    public T remove() {
        T removedData = null;
        if (this.head.next == null) {
            removedData = this.head.data;
            this.head.data = null;

        } else {
            removedData = head.data;
            head = head.next;
        }

        return removedData;
    }

    public T peek() {
        return head.data;
    }

    public boolean isEmpty() {
        return head.data == null;
    }

    @Override
    public String toString() {
        QueueNode<T> n = head;
        String s = "";

        while (n != null) {
            s += n.data + " -> ";
            n = n.next;
        }

        return s;
    }

    public static void main(String[] args) {

        MyQueue<Integer> queue = new MyQueue<Integer>(null);
        queue.add(1);
        queue.add(2);
        queue.add(3);
        System.out.println(queue.toString());

        queue.remove();
        queue.remove();
        queue.remove();
        queue.remove();
        System.out.println(queue.toString());

        System.out.println(queue.isEmpty());
    }
}
