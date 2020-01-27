package patternPrinting;

import java.util.Scanner;

public class Pattern5 {
	
	public static void pattern5() {
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter number of iteration: ");
		int n = scan.nextInt();
		
		for(int i=1;i<=n;i++) {
			for(int k=2;k<=i;k++) {
				System.out.print(" ");
			}
			for(int j=n;j>=i;j--) {
				System.out.print("*");
			}
			System.out.println();
		}
	}

	public static void main(String[] args) {
		
		pattern5();

	}

}
