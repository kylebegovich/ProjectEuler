/**
 * Created by Kyle on 9/18/17
 */
public class Problem6 {


    public static int problem6(int nums) {
        int sumOfSquares = 0;
        int squareOfSum = 0;

        for (int i = 1; i <= nums; i ++) {
            sumOfSquares += (int) Math.pow(i, 2);
            squareOfSum += i;
        }

        squareOfSum = (int) Math.pow(squareOfSum, 2);

        return Math.abs(sumOfSquares - squareOfSum);
    }


    public static void main(String[] args) {
        int answer = problem6(100);
        System.out.println("Problem 6 solution: " + answer);
    }
}
