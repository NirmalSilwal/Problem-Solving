package Lecture2;

import java.util.Scanner;

public class gcd_assignment {

	

	    public static void main(String args[]) {
			
			Scanner sc = new Scanner(System.in);
			long n1 = sc.nextLong();
			long n2 = sc.nextLong();

			long divisor = 0;
			long dividend = 0;
			long rem = 0;

			if (n1 < n2){
				divisor = n1;
				dividend = n2;
			}else{
				divisor = n2;
				dividend = n1;
			}

			while (dividend % divisor != 0){
				rem = dividend % divisor;
				dividend = divisor;
				divisor = rem;
			}
		System.out.println(divisor);
	    }
	}

