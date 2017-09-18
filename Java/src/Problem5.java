import java.util.ArrayList;
import java.util.List;

/**
 * Created by Kyle on 8/23/17
 */
public class Problem5 {


    private static int[] nums = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20};

    private static int problem() {
        int curr = 1;

        for (int n : nums) {
            List<Integer> currFactors = primeFactors(curr);
            List<Integer> nextFactors = primeFactors(n);

            ArrayList<Integer> intersection = new ArrayList<>(nextFactors);
            for (int elem : currFactors) {
                intersection.remove(new Integer(elem));
            }
            currFactors.addAll(intersection);

            curr = 1;
            for (int elem : currFactors) {
                curr *= elem;
            }
        }

        return curr;
    }


    private static List<Integer> primeFactors(int number) {
        int n = number;
        List<Integer> factors = new ArrayList<Integer>();
        for (int i = 2; i <= n; i++) {
            while (n % i == 0) {
                factors.add(i);
                n /= i;
            }
        }
        return factors;
    }


    public static void main(String[] args) {
        int out = problem();
        System.out.println("Problem 5 solution: " + out);
    }
}
