package Lecture2;

import java.util.Scanner;

public class PrimeNumber {

	    public static void main(String args[]) {

			Scanner sc = new Scanner(System.in);
			long num = sc.nextLong();

			for (int i=2; i<=num/2; i++){
				if (num%i == 0){
					System.out.println("Not Prime");
					return;
				}
			}
			System.out.println("Prime");
	    }
	}

