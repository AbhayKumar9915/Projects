package patternPrinting;

import java.util.Scanner;

public class Pattern3 {
	
	public static void pattern3() {
		
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter Iteration number: ");
		int n = scan.nextInt();
		for(int i=1; i<=n;i++) {
			for (int j=1;j<=i;j++) {
				System.out.print("* ");
			}
			System.out.println();
		}
		
		for(int i=1; i<=n-1;i++) {
			for (int j=n-1;j>=i;j--) {
				System.out.print("* ");
			}
			System.out.println();
		}
		
	}

	public static void main(String[] args) {
		
		pattern3();

	}

}
