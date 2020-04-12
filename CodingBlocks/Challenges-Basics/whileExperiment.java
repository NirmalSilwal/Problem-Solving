package Lecture2;

import java.util.Scanner;

public class whileExperiment {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int i=0;
		while(true){
			int n = sc.nextInt();
			System.out.println(i+" "+n);
			i++;
			if (n==4){
				return;
			}
		}
	}

}
