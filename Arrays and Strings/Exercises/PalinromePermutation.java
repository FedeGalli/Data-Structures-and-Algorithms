//given a string check if it's a permutation of a palindrome (no case sensitive and should 
//work with non alphanumeric characters)
public class PalinromePermutation {
    public static boolean palindromePermutation(String s) {
        boolean isOdd = false;
        boolean triggeredOdd = false;
        if (s.length() % 2 == 1) {
            isOdd = true;
        }
        for (int i = 0; i < s.length(); i++) {
            int counter = 0;
            for (int j = 0; j < s.length(); j++) {
                if (s.charAt(i) == s.charAt(j)) {
                    counter++;
                }
            }

            if (counter % 2 == 1) {
                if (isOdd) {
                    if (triggeredOdd) {
                        return false;
                    } else {
                        triggeredOdd = true;
                    }
                } else {
                    return false;
                }
            }
        }

        return true;
    }

    public static void main(String[] args) {

        System.out.println(PalinromePermutation.palindromePermutation("vcav"));
    }
}
