import java.util.ArrayList;
import java.util.List;

/**
 * Created by Kyle on 8/23/17.
 */
public class Problem5 {


    public static void problem() {
    }


    public static List<Integer> primeFactors(int number) {
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
        System.out.println(primeFactors(13650));

    }
}
