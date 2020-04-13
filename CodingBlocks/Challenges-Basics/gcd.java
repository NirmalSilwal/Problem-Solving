package Lecture2;

import java.util.Scanner;

public class gcd {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
        Scanner s=new Scanner(System.in);
        
        int a=s.nextInt();
        int b=s.nextInt();
        
        int dividend=0,divisor=0;
        if(a>b) {
        	dividend=a;
        	divisor=b;
        }else {
        	dividend=b;
        	divisor=a;
        }
        
        while(dividend%divisor!=0) {
        	int rem=dividend%divisor;
        	dividend=divisor;
        	divisor=rem;
        }
        
        System.out.println(divisor);
	}

}