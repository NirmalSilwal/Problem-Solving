package Lecture2;

import java.util.Scanner;

public class PrimePrint {
	
	public static void main(String args[]) {
		// Your Code Here
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		
		boolean is_prime;
		
		for (int i = 2; i <= num; i++) {
			is_prime = is_prime_number(i);
			if (is_prime == true) {
				System.out.println(i);
			}
		}

	}

	public static boolean is_prime_number(int n) {

		for (int i = 2; i <= n / 2; i++) {
			if (n % i == 0) {
				// not prime
				return false;
			}
		}
		return true;
	}
}
