package Lecture2;

import java.util.Scanner;

public class ReverseNumber {
	
    public static void main(String args[]) {
        // Your Code Here
		Scanner sc = new Scanner(System.in);
		long num = sc.nextLong();

		long sum = 0;
		long remainder;
		
		while (num != 0){
			remainder = num % 10;
			sum = sum*10 + remainder ;
			num = num/10;
		}
		System.out.println(sum);
	
    }
}
