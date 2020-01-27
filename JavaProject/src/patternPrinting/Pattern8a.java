package patternPrinting;

import java.util.Scanner;

public class Pattern8a {
	
	public static void pattern8() {
		
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
			for(int l=2;l<=i;l++) {
				System.out.print("*");
			}
			System.out.println();
		}
		
	}

	public static void main(String[] args) {
		
		pattern8();

	}

}
