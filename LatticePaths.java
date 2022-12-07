// https://projecteuler.net/problem=15
// Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
// How many such routes are there through a 20×20 grid?

public class LatticePaths {
    public static void main(String[] args) {
        // To get to the bottom-right from top-left we have to go through equal no. of right and bottom direction ways. So, we have to choose 20 right and 20 bottom paths to get to the final termination point.
        // So,for 20x20 grid, binomial(40, 20) is the answer.
        System.out.print(binomial(40, 20));
    }
    static int binomial(int n, int k){
        if(k==0 || k==n)
            return 1;
        else
            return binomial(n-1, k-1) + binomial(n-1,k);
    }
    
}