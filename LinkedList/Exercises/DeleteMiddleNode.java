//delete a node in the middle
public class DeleteMiddleNode {
    int data;
    DeleteMiddleNode next;

    public DeleteMiddleNode(int data) {
        this.data = data;
        next = null;
    }

    public void append(int data) {

        DeleteMiddleNode n = this;
        while (n.next != null) {
            n = n.next;
        }
        n.next = new DeleteMiddleNode(data);
    }

    public void removeAt(int index) {
        int i = 0;

        DeleteMiddleNode prev = this;
        while (i < index - 1) {
            prev = prev.next;
            i++;

        }
        prev.next = prev.next.next;

    }

    public void deleteMiddleNode() {
        DeleteMiddleNode prev = null;
        DeleteMiddleNode n1 = this;
        DeleteMiddleNode n2 = this.next;

        while(n2.next != null) {
            prev = n1;
            n1 = n1.next;
            n2 = n2.next.next;
        }

        prev.next = n1.next;

    }
    
    @Override
    public String toString() {
        String s = "";
        DeleteMiddleNode n = this;
        while(n != null) {
            
            s += String.valueOf(n.data) + "->";
            n = n.next;
        }

        return s;
    }
    public static void main(String[] args) {

        DeleteMiddleNode list = new DeleteMiddleNode(0);
        list.append(1);
        list.append(2);
        list.append(3);
        list.append(4);
        list.append(5);
        list.deleteMiddleNode();
        System.out.println(list.toString());
    }
}