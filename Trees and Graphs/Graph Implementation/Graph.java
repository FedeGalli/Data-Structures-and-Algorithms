import java.util.Queue;
import java.util.ArrayList;
import java.util.LinkedList;

public class Graph {

    private class GraphNode {
        int data;
        LinkedList<GraphNode> children;
        boolean isVisited;
    
        public GraphNode(int data) {
            this.data = data;
            isVisited = false;
            children = new LinkedList<>();
        }
    
        public void add(GraphNode node) {
            children.add(node);
        }

        public String toString() {
            String s = String.valueOf(data) + "->";

            for (GraphNode n : children) {
                s += n.data + "->";
            }
            return s;
        }
    }
    
    ArrayList<GraphNode> nodes;

    public Graph() {
        nodes = new ArrayList<>();
    }

    public void addNode(int data) {
        GraphNode node = new GraphNode(data);
        if (!exists(node))
            nodes.add(node);
        
    }

    public void addEdge(GraphNode start, GraphNode dest) {
        if (exists(start) && exists(dest)) {
            nodes.get(nodes.indexOf(start)).add(dest);
        }
    }

    public boolean exists(GraphNode node) {
        for(GraphNode n : nodes) {   
            if (n == node)
                return true;
        }

        return false;
    }

    public void print() {

        for (GraphNode n : nodes) {
            System.err.println(n.toString());
        }
    }

    public void visit(int value) {
        System.err.println(value);
    }

    public void depthFirstSearch(GraphNode node) {

        if (node == null) return;

        for (GraphNode curretNode : node.children) {
            visit(curretNode.data);
            curretNode.isVisited = true;
            if (!curretNode.isVisited)
                depthFirstSearch(curretNode);
        }
    }
    
    public void breadthFirstSearch(GraphNode node) {

        Queue<GraphNode> queue = new LinkedList<GraphNode>();

        queue.add(node);

        while(!queue.isEmpty()) {
            GraphNode currentNode = queue.poll();
            if (!currentNode.isVisited) {
                visit(currentNode.data);
                currentNode.isVisited = true;
                
                for (GraphNode n : currentNode.children) { 
                    queue.add(n);
                }
            }
        }
    }

    //Give two nodes, start and end find if they are connected
    public boolean areConnected(GraphNode start, GraphNode end) {

        if (start.data == end.data) return true;

        Queue<GraphNode> bfs = new LinkedList<>();

        bfs.add(start);

        while(!bfs.isEmpty()) {

            GraphNode current = bfs.poll();
            if (!current.isVisited) {

                if (current.data == end.data) return true;

                current.isVisited = true;

                System.out.println(current);
                
                for (GraphNode n : current.children) {
                    System.out.println(n);
                    bfs.add(n);
                }
                    
            }
        }

        return false;

    }

    public GraphNode getNode(int data) {
        for(GraphNode n : nodes) {
            if (n.data == data) {
                return n;
            }
        }

        return null;
    }
    

    public static void main(String[] args) {

        Graph g = new Graph();

        g.addNode(0);
        g.addNode(1);
        g.addNode(2);
        g.addNode(3);
        g.addNode(4);
        g.addNode(5);

        g.addEdge(g.getNode(0), g.getNode(1));
        g.addEdge(g.getNode(0), g.getNode(4));
        g.addEdge(g.getNode(0), g.getNode(5));
        g.addEdge(g.getNode(1), g.getNode(4));
        g.addEdge(g.getNode(1), g.getNode(3));
        g.addEdge(g.getNode(3), g.getNode(2));
        g.addEdge(g.getNode(3), g.getNode(4));
        g.addEdge(g.getNode(2), g.getNode(1));

        System.out.println(g.areConnected(g.getNode(0), g.getNode(2)));

        g.print();
    }
}