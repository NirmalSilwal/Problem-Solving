package Lecture2;

// Take N as input. Print the sum of its odd placed digits and sum of its even placed digits.
//Constraints
//0 < N <= 1000000000

import java.util.Scanner;

public class oddEven {
	
    public static void main(String args[]) {
	
    	Scanner sc = new Scanner(System.in);

		long n = sc.nextLong();
		long temp = n;
		int evenSum = 0;
		int oddSum = 0;
		int count = 1;
		long rem=0;

		while (n!=0){
			if (count %2 != 0){
				rem = n%10;
				oddSum += rem;
				count++;
				n = n/10;
			}
			else{
				rem = n%10;
				evenSum += rem;
				count++;
				n = n/10;
			}
		}

		System.out.println(oddSum);
		System.out.println(evenSum);

    }
}
