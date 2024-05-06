//method to perform compression using the counts of repeated characters. If the compressed string is
//bigger then the original string, return the original string

public class StringCompression {
    public static String stringCompression(String s) {
        char lastChar = s.charAt(0);
        int counter = 1;
        String compressedString = "";

        for (int i = 1; i < s.length(); i++) {
            if (lastChar == s.charAt(i)) {
                counter++;
            } else {
                compressedString += lastChar + String.valueOf(counter);
                lastChar = s.charAt(i);
                counter = 1;
            }
        }

        compressedString += lastChar + String.valueOf(counter);

        if (compressedString.length() >= s.length()) {
            return s;
        }
        else {
            return compressedString;
        }
    }
    public static void main(String[] args) {
        System.out.println(StringCompression.stringCompression("ciaoooooo"));
    }
}
