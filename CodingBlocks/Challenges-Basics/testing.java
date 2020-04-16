package Lecture2;

//testing scope of variables

public class testing {

	public static void main(String[] args) {
		int n = 10;
		int x = check(n);
		System.out.println(n+" "+ x);
	}
	public static int check(int n){
		n = n+10;
		return n;
	}

}
