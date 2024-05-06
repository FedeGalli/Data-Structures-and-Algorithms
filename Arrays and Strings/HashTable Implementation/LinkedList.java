public class LinkedList<T> {
    T data;
    LinkedList<T> next = null;

    public LinkedList() {
        data = null;
    }

    public LinkedList(T item) {
        data = item;
    }

    public void add(T item) {
        if (this.data == null) {
            this.data = item;
        }
        else if (this.next == null)
            this.next = new LinkedList<T>(item);
        else {
            LinkedList<T> curr = this.next;
            while(curr.next != null) {
                curr = curr.next;
            }
    
            curr.next = new LinkedList<T>(item);
        }

    }

    public void removeAt(int index) {
        if (index == 0) {
            this.data = this.next.data;
            this.next = this.next.next;
        }
        else if (index == 1) {
            this.next = this.next.next;
        }
        else {
            int i = 1;
            LinkedList<T> curr = this.next;
            LinkedList<T> prev = null;
            while(i < index) {
                if (i == index - 1) {
                    prev = curr;
                }
                curr = curr.next;
                i++;
            }
    
            prev.next = curr.next;
            
        }
    }

    public void addAt(int index, T item) {
        if (index == 0) {
            this.data = item;
        }
        else if (index == 1) {
            LinkedList<T> tmp = this.next;
            this.next = new LinkedList<T>(item);
            this.next.next = tmp;
        }
        else {
            LinkedList<T> curr = this.next;
            LinkedList<T> prev = null;
    
            int i = 1;
    
            while(i < index) {
                if (i == index - 1) {
                    prev = curr;
                }
                curr = curr.next;
                i++;
            }
            
            prev.next = new LinkedList<T>(item);
            prev.next.next = curr;
        }

    }

    public String toString() {

        LinkedList<T> curr = this.next;
        String s = (String) String.valueOf(this.data);
        while(curr != null) {
            s += (String) String.valueOf(curr.data);
            curr = curr.next;
        }

        return s;
    }

    public static void main(String[] args) throws Exception {

        LinkedList<Integer> list = new LinkedList<Integer>(0);

        list.add(1);
        list.add(2);
        list.add(3);
        list.add(4);
        list.add(5);

        list.addAt(5, 9);
        System.out.println(list);
    }
}

class HashTable {
    LinkedList<Integer>[] data;

    public HashTable() {
        data = new LinkedList[10];

        for (int i = 0; i < 10; i++) {
            data[i] = new LinkedList<Integer>();
        }
    }

    public HashTable(int len) {
        data = new LinkedList[len];

        for (int i = 0; i < len; i++) {
            data[i] = new LinkedList<Integer>();
        }
    }

    private int hashFunction(int input) {
        return input % data.length;
    }

    public void add(int item) {
        data[hashFunction(item)].add(item);
    }


}