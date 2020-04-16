package Lecture2;

import java.util.Scanner;
import java.lang.Math;

public class Boston_Number {
	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);

		boolean bostonNum = false;
		int num = sc.nextInt();
		int numSum = sumOfDigits(num);

		int primeFactorsum = primeFactorFinder(num);

		if (numSum == primeFactorsum) {
			bostonNum = true;
		}

		if (bostonNum) {
			System.out.println("1");
		} else {
			System.out.println("0");

		}

	}

	public static int sumOfDigits(int n) {
		int nsum = 0;

		while (n != 0) {
			nsum += n % 10;
			n = n / 10;
		}

		return nsum;
	}

	
	public static int primeFactorFinder(int n) {

		int factorSum = 0;

		while (n % 2 == 0) {
			factorSum += 2;
			n = n / 2;
		}

		for (int i = 3; i <= n/2; i = i + 2) {

			while (n % i == 0) {
				factorSum = factorSum + sumOfDigits(i);
				n = n / i;
			}
		}

		if (n > 2) {
			factorSum = factorSum + sumOfDigits(n);
		}

		return factorSum;

	}
}