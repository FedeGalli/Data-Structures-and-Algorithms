//implement a method to check if a string has all unique characters

public class IsUnique {
    
    public static boolean isUnique(String s) {
        
        if (s.length() > 128)
            return false;
        boolean[] values = new boolean[128];


        for (int i = 0; i < s.length(); i++) {
            
            int val = s.charAt(i);
            if (!values[val]) {
                values[val] = true;
            } else {
                return false;
            }
        }
        return true;

    }

    public static void main(String[] args) {
        System.out.println(IsUnique.isUnique("clear"));
    }

}
