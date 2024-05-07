//write code to remove duplicates from unsorted linked list

import java.util.HashSet;

public class RemoveDups {
    int data;
    RemoveDups next;

    public RemoveDups(int data) {
        this.data = data;
        next = null;
    }

    public void append(int data) {

        RemoveDups n = this;
        while (n.next != null) {
            n = n.next;
        }
        n.next = new RemoveDups(data);
    }

    public void removeAt(int index) {
        int i = 0;

        RemoveDups prev = this;
        while (i < index - 1) {
            prev = prev.next;
            i++;

        }
        prev.next = prev.next.next;

    }

    // no temp buffer
    public void removeDups() {
        RemoveDups current = this;
        RemoveDups n = this;
        while(current != null) {
            while(n.next != null) {
                if (n.next.data == current.data) {
                    n.next = n.next.next;
                }
                else {
                    n = n.next;
                }
                
            }
            current = current.next;
        }
    }

        // no temp buffer
    public void removeDupsWithBuffer() {
        HashSet<Integer> set = new HashSet<>();
        RemoveDups n = this;
        RemoveDups prev = null;
        while (n != null) {

            if(set.contains(n.data)) {
                prev.next = n.next;
            } else {
                set.add(n.data);
                prev = n;
            }
            n = n.next;
        }
    }
    
    @Override
    public String toString() {
        String s = "";
        RemoveDups n = this;
        while(n != null) {
            
            s += String.valueOf(n.data) + "->";
            n = n.next;
        }

        return s;
    }
    public static void main(String[] args) {

        RemoveDups list = new RemoveDups(0);
        list.append(1);
        list.append(0);
        list.append(0);
        list.removeDupsWithBuffer();
        System.out.println(list.toString());
    }
}