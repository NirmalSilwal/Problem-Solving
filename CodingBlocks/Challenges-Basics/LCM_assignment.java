package Lecture2;

import java.util.Scanner;

public class LCM_assignment {

	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		long n1 = sc.nextLong();
		long n2 = sc.nextLong();

		long gcd = compute_gcd(n1, n2);
		
		long lcm = (n1 * n2) / gcd;

		System.out.println(lcm);

	}

	public static long compute_gcd(long n1, long n2) {

		long divisor = 0, dividend = 0, rem = 0;

		if (n1 < n2) {
			divisor = n1;
			dividend = n2;
		} else {
			divisor = n2;
			dividend = n1;
		}

		while (dividend % divisor != 0) {
			rem = dividend % divisor;
			dividend = divisor;
			divisor = rem;
		}

		return divisor;
	}
}
