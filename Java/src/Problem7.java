/**
 * Created by Kyle on 9/19/17.
 */
public class Problem7 {


    public static int prime10001() {
        int[] primes = Euler.primeSieve(10000000);
        return primes[10000];
    }


    public static void main(String[] args) {
        int answer = prime10001();
        System.out.println("Problem 7 solution: " + answer);

    }
}
