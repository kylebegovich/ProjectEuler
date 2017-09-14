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
        if (!Euler.isPalendrome("9009")) return false;
        if (!Euler.isPalendrome("girafarig")) return false;
        if (!Euler.isPalendrome("wew")) return false;
        if (!Euler.isPalendrome("holy hecc cceh holy")) return false;
        if (!Euler.isPalendrome("")) return false;
        if (!Euler.isPalendrome("    ")) return false;



        if (Euler.isPalendrome("51422678")) return false;
        if (Euler.isPalendrome("mzshrv")) return false;
        if (Euler.isPalendrome("wow writing test cases is fun")) return false;
        if (Euler.isPalendrome("inside job")) return false;

        return true;
    }

}
