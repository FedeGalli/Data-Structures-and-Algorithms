//given a linked list, which might contain a loop, implement an algo that returns the node at the beginning of the loop
//
public class LoopDetection {
    int data;
    LoopDetection next;

    public LoopDetection(int data) {
        this.data = data;
        next = null;
    }

    public void append(int data) {

        LoopDetection n = this;
        while (n.next != null) {
            n = n.next;
        }
        n.next = new LoopDetection(data);
    }

    public void append(LoopDetection data) {

        LoopDetection n = this;
        while (n.next != null) {
            n = n.next;
        }
        n.next = data;
    }

    public static LoopDetection loopDetection(LoopDetection n) {

        LoopDetection fastPointer = n;
        LoopDetection slowPointer = n;

        while(fastPointer != null && slowPointer != null) {
            fastPointer = fastPointer.next.next;
            slowPointer = slowPointer.next;

            //here i know that fast pointer and slow pointer are LOOPSIZE - k distance from each other
            if(fastPointer == slowPointer) {
                break;
            }
        }

        if(fastPointer == null || slowPointer == null) {
            return null;
        }

        slowPointer = n;

        while(slowPointer != null) {
            if (slowPointer == fastPointer) {
                break;
            }
            
            slowPointer = slowPointer.next;
            fastPointer = fastPointer.next;

        }

        return slowPointer;
    }

    @Override
    public String toString() {
        String s = "";
        LoopDetection n = this;
        while(n != null) {
            
            s += String.valueOf(n.data) + "->";
            n = n.next;
        }

        return s;
    }
    public static void main(String[] args) {

        LoopDetection tmpNode = new LoopDetection(10);
        tmpNode.append(100);
        tmpNode.append(1000);
        tmpNode.append(tmpNode);
        LoopDetection list1 = new LoopDetection(0);
        list1.append(4);
        list1.append(tmpNode);
        System.out.println(loopDetection(list1).data);
    }
}