//you have two numbers represented by a linked list, the digits are stored in reverse order (extension of the problem with forward order)
public class SumLists {
    int data;
    SumLists next;

    public SumLists(int data) {
        this.data = data;
        next = null;
    }

    public void append(int data) {

        SumLists n = this;
        while (n.next != null) {
            n = n.next;
        }
        n.next = new SumLists(data);
    }

    public void removeAt(int index) {
        int i = 0;

        SumLists prev = this;
        while (i < index - 1) {
            prev = prev.next;
            i++;

        }
        prev.next = prev.next.next;

    }

    public static SumLists sumListsReverse(SumLists n1, SumLists n2) {

        SumLists result = null;
        SumLists head = null;
        int rest = 0;


        while(n1 != null || n2 != null) {
            if(result == null) {
                result = new SumLists(((n1.data + n2.data)) % 10);
                rest = (n1.data + n2.data) / 10;
            }
            else {
                if (n1 == null) {
                    result.next = new SumLists(((n2.data + rest)) % 10);
                } else if (n2 == null) {
                    result.next = new SumLists(((n1.data + rest)) % 10);
                } else {
                    result.next = new SumLists(((n1.data + n2.data + rest)) % 10);
                    rest = (n1.data + n2.data + rest) / 10;
                }
                
                if (head == null) {
                    head = result;
                }

                result = result.next;
            }

            if (n1 != null)
                n1 = n1.next;
            if (n2 != null)
                n2 = n2.next;
        }
        if (rest > 0) {
            result.next = new SumLists(1);
        }

        return head;
    }

    @Override
    public String toString() {
        String s = "";
        SumLists n = this;
        while(n != null) {
            
            s += String.valueOf(n.data) + "->";
            n = n.next;
        }

        return s;
    }
    public static void main(String[] args) {

        SumLists n1 = new SumLists(9);
        n1.append(9);
        SumLists n2 = new SumLists(5);
        System.out.println(sumListsReverse(n1, n2).toString());
    }
}