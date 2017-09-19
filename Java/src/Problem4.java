/**
 * Created by Kyle on 8/23/17.
 */
public class Problem4 {


    private static int bigOlePalindrome() {

        int currMax = 0;

        for (int i = 800; i < 1000; i ++) {
            for (int j = 800; j < 1000; j ++) {
                if (i*j > currMax && Euler.isPalindrome((i*j) + "")) {
                    currMax = i*j;
                }
            }
        }

        return currMax;
    }


    public static void main(String[] args) {
        int biggest = bigOlePalindrome();
        System.out.println("Problem 4 solution: " + biggest);
    }
}
