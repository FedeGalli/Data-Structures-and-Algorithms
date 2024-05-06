//write a method to remove the blank spaces with '%20'

public class URLify {

    public static int countNewStringLength(char[] s, int length) {

        int count = 0;
        int i = 0;
        boolean currentOnBlankChar = false;
        while (i < length) {
            if (s[i] == ' ' && !currentOnBlankChar) {
                count = count + 3;
                currentOnBlankChar = true;
            }else if (!(s[i] == ' ' && currentOnBlankChar)) {
                count++;
                currentOnBlankChar = false;
            }
            i++;
        }

        return count;
    }

    public static char[] urlify(char[] s, int length) {
        char[] newString = new char[countNewStringLength(s, length)];

        int i = 0;
        int j = 0;
        boolean currentOnBlankChar = false;
        while (i < newString.length) {
            if (s[j] == ' ' && !currentOnBlankChar) {
                currentOnBlankChar = true;
                newString[i] = '%';
                newString[i+1] = '2';
                newString[i+2] = '0';
                i += 3;
            } else if (!(s[j] == ' ' && currentOnBlankChar)) {
                currentOnBlankChar = false;
                newString[i] = s[j];
                i++;
            }
            j++;
        }

        return newString;
    }

    public static void main(String[] args) {
        char[] x = {' ', 'a', 'i', ' ', ' ', 'x', ' '};
        System.out.println(URLify.urlify(x, x.length));
    }
    
}
