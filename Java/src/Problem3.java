/**
 * Created by Kyle on 8/23/17.
 */
public class Problem3 {


    public static long biggestPrimeFactor(long value) {

        // make sure it's got no even factors left
        while (value % 2 == 0) {
            value /= 2;
        }
        
        long curr = 3;

        // once value is less than the square of the primes it's no longer divisible by, it's guaranteed to be prime
        while (value > Math.pow(curr, 2)) {
            if (value % curr == 0) {
                value /= curr;
            } else {

                // increment to potentially next prime
                curr += 2;
            }
        }

        return value;
    }


    public static void main(String[] args) {
        System.out.println("Problem");
        long value = 600851475143L;
        System.out.println("Answer: " + biggestPrimeFactor(value));
    }
}
