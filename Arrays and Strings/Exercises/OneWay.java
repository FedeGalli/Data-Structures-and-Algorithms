//there are three types of edits that can be performed on strings: insert a char, remove a char, or replace a char. Given two strings, 
//write a function to check if they are one edit(or zero edits) away.
public class OneWay {
    public static boolean oneWay(String s1, String s2) {

        if(s2.length() > s1.length() + 1 || s2.length() < s1.length() - 1) {
            return false;
        }

        boolean isInsert = false;
        boolean isReplace = false;
        boolean isRemove = false;

        //replace same length
        //insert s2 = s1 + 1
        //remove s2 = s1 - 1

        for(int i = 0; i < s1.length(); i++) {
            if (i == s2.length())
                return true;
            if (isRemove) {
                if (s1.charAt(i) != s2.charAt(i-1)) {
                    return false;
                }
            } else if (isReplace) {
                if (s1.charAt(i) != s2.charAt(i)) {
                    return false;
                }
            } else if (isInsert) {
                if (s1.charAt(i-1) != s2.charAt(i)) {
                    return false;
                }                
            }
            else if (s1.charAt(i) != s2.charAt(i)) {
                if (s1.length() == s2.length()) {
                    isReplace = true;
                }
                else if (s1.length() > s2.length()) {
                    isRemove = true;
                } else {
                    isInsert = true;
                }
            }
        }

        return true;

    }

    public static void main(String[] args) {

        System.out.println(OneWay.oneWay("pale", "pales"));
    }
}
