/**
 * Created by Kyle on 9/20/17.
 */
public class Problem10 {


    public static long problem(int max) {
        int[] primes = Euler.primeSieve(max);
        long sum = 0;
        for (int i = 0; i < primes.length; i ++) {
            sum += primes[i];
        }
        return sum;
    }


    public static void main(String[] args) {
        long sum = problem(2000000);
        System.out.println("Problem 10 solution: " + sum);

    }
}
