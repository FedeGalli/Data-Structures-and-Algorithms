//implement a function to check if a linked list is a palindrome
//write code to remove duplicates from unsorted linked list
public class Palindrome {
    int data;
    Palindrome next;

    public Palindrome(int data) {
        this.data = data;
        next = null;
    }

    public void append(int data) {

        Palindrome n = this;
        while (n.next != null) {
            n = n.next;
        }
        n.next = new Palindrome(data);
    }

    public static Palindrome reverseLinkedList(Palindrome n) {

        Palindrome head = null;
        while(n != null) {

            Palindrome node = new Palindrome(n.data);
            node.next = head;
            head = node;
            
            n = n.next;
        }

        return head;
    }

    public static boolean isPalindrome(Palindrome n) {

        Palindrome reversed = reverseLinkedList(n);
        while(reversed != null) {
            if (reversed.data != n.data) {
                return false;
            }

            reversed = reversed.next;
            n = n.next;
        }

        return true;
    }
    
    @Override
    public String toString() {
        String s = "";
        Palindrome n = this;
        while(n != null) {
            
            s += String.valueOf(n.data) + "->";
            n = n.next;
        }

        return s;
    }
    public static void main(String[] args) {

        Palindrome list = new Palindrome(0);
        list.append(4);
        list.append(4);
        System.out.println(isPalindrome(list));
    }
}