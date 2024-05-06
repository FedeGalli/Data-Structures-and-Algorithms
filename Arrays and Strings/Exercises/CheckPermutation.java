//given two strings, write a method to decide if one is a permutation of the other
//aac caa true
//abc efg false
public class CheckPermutation {

    public static String sort(String s) {

        char[] characters = s.toCharArray();

        java.util.Arrays.sort(characters);

        return new String(characters);
    }

    public static boolean checkPermutation(String s1, String s2) {
        if (s1.length() != s2.length())
            return false;

        if (sort(s1).equals(sort(s2)))
            return true;
        
        return false;
    }
    public static void main(String[] args) {
        System.out.println(CheckPermutation.checkPermutation("abc", "bca"));
    }
    
}
