package patternPrinting;

import java.util.Scanner;

public class Pattern2 {
	
	public static void pattern2() {
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter Iteration Number: ");
		int n = scan.nextInt();
		for(int i=1; i<=n;i++) {
			for (int j=n;j>=i;j--) {
				System.out.print("* ");
			}
			System.out.println();
		}
	}

	public static void main(String[] args) {
		
		pattern2();

	}

}
