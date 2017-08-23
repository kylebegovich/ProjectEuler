/**
 * Created by Kyle on 8/23/17.
 */
public class Problem1 {


    public static int fizzbuzz(int range, int[] divisBy) {
        int sum = 0;

        for (int i = 0; i < range; i ++) {
            for (int divis : divisBy) {
                if (i % divis == 0) {
                    sum += i;
                    break;
                }
            }
        }

        return sum;
    }


    public static void main(String[] args) {
        System.out.println("Problem 1");
        int[] divisBy = {3, 5};
        System.out.println("Answer: " + fizzbuzz(1000, divisBy));
    }
}
