package Lecture2;

import java.lang.Math;

public class primeFactors {

	public static void main(String[] args) {

		int n = 85;
		int sum = 0;

		while (n % 2 == 0) {
			System.out.println(2);
			sum += 2;
			n = n / 2;
		}

		for (int i=3; i<=Math.sqrt(n);i=i+2){
			while (n%i == 0){
				System.out.println(i);
				sum += i;
				n = n/i;
			}
		}
		
		if (n>2){
			System.out.println(n);
			sum += n;
		}
		System.out.println("sum of all prime factors is: "+sum);
	}
}
