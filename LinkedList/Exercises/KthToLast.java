//write code to remove duplicates from unsorted linked list
public class KthToLast {
    int data;
    KthToLast next;

    public KthToLast(int data) {
        this.data = data;
        next = null;
    }

    public void append(int data) {

        KthToLast n = this;
        while (n.next != null) {
            n = n.next;
        }
        n.next = new KthToLast(data);
    }

    public void removeAt(int index) {
        int i = 0;

        KthToLast prev = this;
        while (i < index - 1) {
            prev = prev.next;
            i++;

        }
        prev.next = prev.next.next;

    }

    // temporary buffer
    public int kthToLast(KthToLast head, int k) {

        if(head == null) 
            return 0;

        int index = kthToLast(head.next, k) + 1;
        if(index == k) {
            System.out.println("element is " + head.data);
        }

        return index;
        
    }
    
    @Override
    public String toString() {
        String s = "";
        KthToLast n = this;
        while(n != null) {
            
            s += String.valueOf(n.data) + "->";
            n = n.next;
        }

        return s;
    }
    public static void main(String[] args) {

        KthToLast list = new KthToLast(0);
        list.append(1);
        list.append(0);
        list.append(3);
        list.append(4);
        list.kthToLast(list, 3);
    }
}