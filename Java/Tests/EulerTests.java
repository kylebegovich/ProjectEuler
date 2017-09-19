/**
 * Created by Kyle on 8/24/17.
 */
public class EulerTests {

    public static void main(String[] args) {
        testAll();
    }

    private static void testAll() {

    }

    private static boolean testIsPalendrome() {
        if (!Euler.isPalindrome("9009")) return false;
        if (!Euler.isPalindrome("girafarig")) return false;
        if (!Euler.isPalindrome("wew")) return false;
        if (!Euler.isPalindrome("holy hecc cceh holy")) return false;
        if (!Euler.isPalindrome("")) return false;
        if (!Euler.isPalindrome("    ")) return false;



        if (Euler.isPalindrome("51422678")) return false;
        if (Euler.isPalindrome("mzshrv")) return false;
        if (Euler.isPalindrome("wow writing test cases is fun")) return false;
        if (Euler.isPalindrome("inside job")) return false;

        return true;
    }

}
