import java.util.Arrays;

/**
 * Created by Kyle on 8/24/17.
 */
public class EulerTests {


    public static void main(String[] args) {
        testAll();
    }


    private static void testAll() {
        int countTestsFailed = 0;
        int countCasesFailed = 0;

        int currFailed = testIsPalendrome();
        if (currFailed != 0) {
            System.out.println("testIsPalendrome() failed " + currFailed + " / X tests");
            countTestsFailed ++;
            countCasesFailed += currFailed;
        }

        currFailed = testPrimeSieve();
        if (currFailed != 0) {
            System.out.println("testPrimeSieve() failed " + currFailed + " / X tests");
            countTestsFailed ++;
            countCasesFailed += currFailed;
        }

        // figure out a way to iterate these instead of copy pasting them all

        if (countTestsFailed != 0) {
            System.out.println("Failed " + countTestsFailed + " / X function tests");
            System.out.println("Failed " + countCasesFailed + " / X total test cases");
        } else {
            System.out.println("All Tests Passed!");
        }
    }


    private static int testIsPalendrome() {
        int countFailed = 0;

        if (!Euler.isPalindrome("9009")) countFailed ++;
        if (!Euler.isPalindrome("girafarig")) countFailed ++;
        if (!Euler.isPalindrome("wew")) countFailed ++;
        if (!Euler.isPalindrome("holy hecc cceh holy")) countFailed ++;
        if (!Euler.isPalindrome("")) countFailed ++;
        if (!Euler.isPalindrome("    ")) countFailed ++;



        if (Euler.isPalindrome("51422678")) countFailed ++;
        if (Euler.isPalindrome("mzshrv")) countFailed ++;
        if (Euler.isPalindrome("wow writing test cases is fun")) countFailed ++;
        if (Euler.isPalindrome("inside job")) countFailed ++;

        return countFailed;
    }


    private static int testPrimeSieve() {
        int countFailed = 0;

        if (Euler.primeSieve(10).length != 4) countFailed ++;
        if (Euler.primeSieve(100).length != 25) countFailed ++;
        if (Euler.primeSieve(1000).length != 168) countFailed ++;
        if (Euler.primeSieve(10000).length != 1229) countFailed ++;

        int[] primeTest1 = {};
        if (!Arrays.equals(Euler.primeSieve(1), primeTest1)) countFailed ++;
        int[] primeTest2 = {2};
        if (!Arrays.equals(Euler.primeSieve(2), primeTest2)) countFailed ++;
        int[] primeTest3 = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
        if (!Arrays.equals(Euler.primeSieve(30), primeTest3)) countFailed ++;

        return countFailed;
    }

}
