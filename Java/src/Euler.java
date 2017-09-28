/**
 * Created by Kyle on 8/24/17.
 */
public class Euler {

    private static String join(String[] words, String separator) {
        StringBuilder out = new StringBuilder("");

        for (int i = 0; i < words.length; i ++) {
            out.append(words[i]);
            if (i != words.length-1) {
                out.append(separator);
            }
        }

        return out.toString();
    }


    public static String numToWords(int num) {
        if (num == 0) {return "Zero";}

        String[] units = {"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
        String[] teens = {"", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
                "Seventeen", "Eighteen", "Nineteen"};
        String[] tens = {"", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy",
                "Eighty", "Ninety"};
        String[] thousands = {"", "Thousand", "Million", "Billion", "Trillion", "Quadrillion",
                "Quintillion", "Sextillion", "Septillion", "Octillion",
                "Nonillion", "Decillion", "Undecillion", "Duodecillion",
                "Tredecillion", "Quattuordecillion", "Sexdecillion",
                "Septendecillion", "Octodecillion", "Novemdecillion",
                "Vigintillion"};

        StringBuffer strNum = new StringBuffer(Integer.toString(num));
        StringBuffer words = new StringBuffer();

        // not even close to done yet :(
        while (strNum.length() > 0) {

        }


        return words.toString();
    }

    public static boolean isPalindrome(String toCheck) {
        return toCheck.length() <= 1 || toCheck.equals(new StringBuffer(toCheck).reverse().toString());
    }

    public static int[] primeSieve(int max) {
        boolean[] isComposite = new boolean[max + 1];
        for (int i = 2; i * i <= max; i++) {
            if (!isComposite [i]) {
                for (int j = i; i * j <= max; j++) {
                    isComposite [i*j] = true;
                }
            }
        }
        int numPrimes = 0;
        for (int i = 2; i <= max; i++) {
            if (!isComposite [i]) numPrimes++;
        }
        int [] primes = new int [numPrimes];
        int index = 0;
        for (int i = 2; i <= max; i++) {
            if (!isComposite [i]) primes [index++] = i;
        }
        return primes;
    }
}
