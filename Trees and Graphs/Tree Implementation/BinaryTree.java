import java.util.ArrayList;
import java.util.LinkedList;

public class BinaryTree {
    private class TreeNode {
        int data;
        TreeNode left;
        TreeNode right;

        public TreeNode(int data) {
            this.data = data;
        }
    }


    TreeNode root;

    public BinaryTree(int data) {
        root = new TreeNode(data);
    }

    public void inOrderTraversal(TreeNode n) {
        if (n != null) {
            inOrderTraversal(n.left);
            System.out.println(n.data);
            inOrderTraversal(n.right);
        }
    }

    public void addAt(int src, int data, boolean isLeft) {
        addAt(root, src, data, isLeft);
    }

    public void addAt(TreeNode node, int src, int data,boolean isLeft) {

        if(node == null) return;

        if (node.data == src) {
            if (isLeft)
                node.left = new TreeNode(data);
            else
                node.right = new TreeNode(data);
            
            return;
        }   

        addAt(node.left, src, data, isLeft);
        addAt(node.right, src, data, isLeft);

    }


    //Given a sorted array (increasing order), calculate the minimum height binary search tree
    public TreeNode minimalBinarySearchTree(int[] array) {
        return minimalBinarySearchTree(array, 0, array.length - 1);
    }
    public TreeNode minimalBinarySearchTree(int[] array, int start, int end) {

        if (end < start)
            return null;

        
        int mid = (start + end) / 2;
        TreeNode n = new TreeNode(array[mid]);

        n.left = minimalBinarySearchTree(array, start, mid - 1);
        n.right = minimalBinarySearchTree(array, mid + 1, end);

        return n;
    }

    //Given a binary tree, craete a linked list of all the nodes at each depth
    public ArrayList<LinkedList<TreeNode>> listOfDeps(BinaryTree tree) {

        int index = 0;
        ArrayList<LinkedList<TreeNode>> depthList = new ArrayList<>();
        
        listOfDeps(tree.root, index, depthList);

        return depthList;
    }

    public void listOfDeps(TreeNode node, int index, ArrayList<LinkedList<TreeNode>> depthList) {
        if(node == null) return;

        if (index >= depthList.size() || index == 0)
            depthList.add(new LinkedList<>());

        depthList.get(index).add(node);
        index++;
        listOfDeps(node.left, index, depthList);
        listOfDeps(node.right, index, depthList);
    }

    public void print(TreeNode node) {
        if (node == null)
            return;
        System.err.println(node.data);
        print(node.left);
        print(node.right);
    }

    public void print() {
        if (root == null)
            return;
        System.err.println(root.data);
        print(root.left);
        print(root.right);
    }




    public static void main (String[] args) {
        BinaryTree t = new BinaryTree(0);
        

        //exercise Given a sorted array (increasing order), calculate the minimum height binary search tree
        //int[] test = {0, 1, 2, 3, 4, 5};
        //t.print(t.minimalBinarySearchTree(test));


        //exercise Given a binary tree, craete a linked list of all the nodes at each depth
        t.addAt(0, 1, true);
        t.addAt(0, 2, false);
        t.addAt(1, 3, true);
        t.addAt(1, 4, false);
        t.addAt(2, 5, false);
        t.addAt(5, 6, true);

        ArrayList<LinkedList<TreeNode>> result = t.listOfDeps(t);
        int i = 0;
        for (LinkedList<TreeNode> linkedList : result) {
            System.err.println("List" + i++);
            for (TreeNode node : linkedList) {
                System.err.println(node.data);
            }
        }

    }
}
