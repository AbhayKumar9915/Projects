package patternPrinting;

import java.util.Scanner;

public class Pattern1 {

	public static void pattern() {
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter Iteration number: ");
		int n = scan.nextInt();
		for(int i=1; i<=n;i++) {
			for (int j=1;j<=i;j++) {
				System.out.print("* ");
			}
			System.out.println();
		}
	
	
	}
	
	public static void main(String[] args) {
		
		pattern();

	}

}
