/**
 * Created by Kyle on 8/23/17.
 */
public class Problem2 {


    public static int evenFib(int range) {
        int sum = 2;
        int a = 2;
        int b = 3;
        while (a < range && b < range) {

            // increment 3 times (every third fib is even)
            a += b;
            b += a;
            a += b;

            // swap the values
            int temp = a;
            a = b;
            b = temp;

            // add to sum
            sum += a;
        }

        return sum;
    }


    public static void main(String[] args) {
        System.out.println("Problem 2");
        System.out.println("Answer: " + evenFib(4000000));
    }
}
