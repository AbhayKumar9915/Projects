package patternPrinting;

import java.util.Scanner;

public class Pattern6 {
	
	public static void pattern6() {
		
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter number of iteration: ");
		int n = scan.nextInt();
		
		for(int i=1;i<=n;i++) {
			for (int k=n-1;k>=i;k--) {
				System.out.print(" ");
			}
			for (int j =1;j<=i;j++) {
				System.out.print("*");
			}
			System.out.println();
		}
		
		for(int i=1;i<=n-1;i++) {
			for(int k=1;k<=i;k++) {
				System.out.print(" ");
			}
			for(int j=n-1;j>=i;j--) {
				System.out.print("*");
			}
			System.out.println();
		}
		
	}

	public static void main(String[] args) {
		
		pattern6();

	}

}
