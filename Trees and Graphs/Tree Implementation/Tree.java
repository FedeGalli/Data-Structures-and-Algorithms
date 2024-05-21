public class Tree {
    private class Node {
        int data;
        Node[] children;

    }

    Node root;

    public Tree() {
        root = new Node();
    }
}