package myPackage;

//Using Recursion

public class FibonacciS{
	
	static int n1=1,n2=1,n3=0;
	static void printFib(int n) {
		if(n>2) {
			n3=n1+n2;
			n1=n2;
			n2=n3;
			System.out.print(" "+n3);
			printFib(n-1);
		}
	}
	public static void main(String[] args) {
		
		System.out.print(1+" "+1);
		printFib(10);
	}
}
