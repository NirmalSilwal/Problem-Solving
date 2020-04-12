package Lecture2;

import java.util.Scanner;

//Given a list of numbers, stop processing input after the cumulative sum of all the 
//input becomes negative.


public class SimpleInput {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int sum = 0;
		Scanner sc = new Scanner(System.in);
		
		while(true){
			int num = sc.nextInt();
			sum += num;
			if (sum>0){
				System.out.println(num);
			}
			else{
				return;
			}
		}

	}

}
