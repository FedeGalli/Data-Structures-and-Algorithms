//wite a methon to partition a linked list given a number k. All the numbers smaller then k should appear in the left side part of the linkedlist
public class Partition {
    int data;
    Partition next;

    public Partition(int data) {
        this.data = data;
        next = null;
    }

    public void append(int data) {

        Partition n = this;
        while (n.next != null) {
            n = n.next;
        }
        n.next = new Partition(data);
    }

    public void removeAt(int index) {
        int i = 0;

        Partition prev = this;
        while (i < index - 1) {
            prev = prev.next;
            i++;

        }
        prev.next = prev.next.next;

    }

    public Partition partition(int k) {
        Partition n = this;
        Partition leftSide = null;
        Partition rightSide = null;
        Partition lHead = null;
        Partition rHead = null;
        while(n != null) {
            if (n.data < k) {
                if (leftSide == null)
                    leftSide = new Partition(n.data);
                else {
                    leftSide.next = new Partition(n.data);
                    if (lHead == null) {
                        lHead = leftSide;
                    }
                    leftSide = leftSide.next;
                }
            }
            else {
                if (rightSide == null)
                    rightSide = new Partition(n.data);
                else {
                    rightSide.next = new Partition(n.data);
                    if (rHead == null) {
                        rHead = rightSide;
                    }
                    rightSide = rightSide.next;
                }
            }
            n = n.next;
        }

        leftSide.next = rHead;

        return lHead;
    }
    
    @Override
    public String toString() {
        String s = "";
        Partition n = this;
        while(n != null) {
            
            s += String.valueOf(n.data) + "->";
            n = n.next;
        }

        return s;
    }
    public static void main(String[] args) {

        Partition list = new Partition(0);
        list.append(1);
        list.append(6);
        list.append(5);
        list.append(4);
        System.out.println(list.partition(5).toString());
    }
}