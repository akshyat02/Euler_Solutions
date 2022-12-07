// https://projecteuler.net/problem=57
// In the first one-thousand expansions of 2^(1/2), how many fractions contain a numerator with more digits than the denominator?

import java.math.*;
public class SquareRootConvergents {
    public static void main(String[] args) {
        int c=0, i=1000;
        BigInteger num = BigInteger.valueOf(0L);
        BigInteger den = BigInteger.valueOf(1L);
        BigInteger temp =  num;
        while(i>0){
            temp = den.multiply(BigInteger.valueOf(2L)).add(num);
            num = den;
            den = temp;
            if (num.add(den).toString().length() > den.toString().length())
				c++;
        }
        System.out.println(c);
    }

}
