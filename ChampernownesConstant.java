// https://projecteuler.net/problem=40
// An irrational decimal fraction is created by concatenating the positive integers:
// 0.123456789101112131415161718192021...
// It can be seen that the 12th digit of the fractional part is 1.
// If dn represents the nth digit of the fractional part, find the value of the following expression.
// d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

public class ChampernownesConstant {
    public static void main(String[] args) {
        System.out.println(prodUptoNth(6));
    }
    static int prodUptoNth(int n){//0<n=6
        int mul=1;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 1000000; i++) {
            sb.append(i);
        }
        for (int i = 0; i < n; i++) {
            mul*=sb.charAt((int) Math.pow(10, i))-'0';
        }
        return mul;
    }
}
