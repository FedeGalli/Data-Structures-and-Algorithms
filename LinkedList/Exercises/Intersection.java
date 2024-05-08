//given two singly linked list, determine if the two lists intersect. Return the intersection node
//
public class Intersection {
    int data;
    Intersection next;

    public Intersection(int data) {
        this.data = data;
        next = null;
    }

    public void append(int data) {

        Intersection n = this;
        while (n.next != null) {
            n = n.next;
        }
        n.next = new Intersection(data);
    }

    public void append(Intersection data) {

        Intersection n = this;
        while (n.next != null) {
            n = n.next;
        }
        n.next = data;
    }

    public static Intersection isIntersecting(Intersection n1, Intersection n2) {

        while(n1 != null ) {
            Intersection n2Tmp = n2;
            while(n2Tmp != null) {
                if (n1 == n2Tmp) {
                    return n1; 
                }
                n2Tmp = n2Tmp.next;
            }
            n1 = n1.next;
        }

        return null;
    }
    
    @Override
    public String toString() {
        String s = "";
        Intersection n = this;
        while(n != null) {
            
            s += String.valueOf(n.data) + "->";
            n = n.next;
        }

        return s;
    }
    public static void main(String[] args) {

        Intersection tmpNode = new Intersection(100);

        Intersection list1 = new Intersection(0);
        list1.append(4);
        list1.append(tmpNode);
        list1.append(42);

        Intersection list2 = new Intersection(0);
        list2.append(10);
        list2.append(tmpNode);
        System.out.println(isIntersecting(list1, list2).data);
    }
}