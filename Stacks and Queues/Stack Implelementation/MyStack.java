public class MyStack<T> {
    private static class StackNode<T> {
        private T data;
        private StackNode<T> next;

        public StackNode(T data) {
            this.data = data;
            this.next = null;
        }
    }



    private StackNode<T> head;

    public MyStack() {
        this.head = new StackNode<T>(null);
    }


    public T pop() {

        if (this.head.next == null) {
            this.head.data = null;
            return null;
        }

        T firstElem = this.head.data;
        this.head = this.head.next;

        return firstElem;

    }

    public void push(T data) {

        if (head.data == null) {
            head.data = data;
        } else {

            StackNode<T> newNode = new StackNode<T>(data);
            newNode.next = head;
            head = newNode;
        }



    }

    public T pick() {

        T firstElem = this.head.data;

        return firstElem;

    }

    public boolean isEmpty() {

        return head.data == null;

    }

    @Override
    public String toString() {
        StackNode<T> n = head;
        String s = "";

        while (n != null) {
            s += n.data + " -> ";
            n = n.next;
        }

        return s;
    }

    public static void main(String[] args) {

        MyStack<Integer> stack = new MyStack<Integer>();
        stack.push(0);
        stack.push(1);
        stack.push(2);
        System.out.println(stack.toString());

        stack.pop();
        stack.pop();
        stack.pop();
        stack.pop();
        stack.push(10);
        System.out.println(stack.toString());
    }


}
