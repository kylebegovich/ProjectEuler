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

        String[] words = {};
        String strNum = Integer.toString(num);
        int strLen = strNum.length();

        // not even close to done yet :(


        return join(words, " ");
    }

}
