package test;

public class Loops {

	public static void main(String[] args) {
		int a = 5;
		char b = 'S';
		float c = (float) 2.50;
		
		String str1 = "Java Programming";
		System.out.println("Data Types");
		System.out.println(a);
		System.out.println(b);
		System.out.println(c);
		System.out.println(str1);
		System.out.println("For Loop");
		
		for (int i=1; i<=a; ++i ){
			System.out.println(i);
		}
		
		System.out.println("If-Else Condition");
		if(b == 's') {
			System.out.println("Passed");
		}
		else {
			System.out.println("Failed");
			
		}
    }
}
