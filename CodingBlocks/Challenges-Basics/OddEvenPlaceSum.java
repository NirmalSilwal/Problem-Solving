package Lecture2;
import java.util.Scanner;

public class OddEvenPlaceSum {
    public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		long n = sc.nextLong();
		
		int oddSum = 0;
		int evenSum = 0;
		int length = 0;
		
		String numStr = Long.toString(n);
		
		while (n!=0){
			n = n/10;
			length++;
		}
		System.out.println("length "+length);
		for (int i=0;i<length;i++){
			
			if (i%2 != 0){
				int evenNumber = Character.getNumericValue(numStr.charAt(i));
				evenSum += evenNumber;
			}else{
				int oddNumber = Character.getNumericValue(numStr.charAt(i));
				oddSum += oddNumber;
			}
		}
		
		System.out.println(evenSum);
		System.out.println(oddSum);
    }
}