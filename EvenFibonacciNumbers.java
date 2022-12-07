// https://projecteuler.net/problem=2
// Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
// 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
// By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

public class EvenFibonacciNumbers {
    public static void main(String[] args) {
        System.out.println(fibo(4000000));
    }
    static int fibo(int n){
        int i=1, j=2, k=0, sum=0;
        while(j<n){
            if(j%2==0) sum+=j;
            k=i+j;
            i=j;
            j=k;
        }
        return sum;
    }
    
}