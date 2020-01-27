package patternPrinting;

import java.util.Scanner;

public class Pattern9 {
	
	public static void pattern9() {
		
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter number of iteration: ");
		int n = sc.nextInt();
		for(int i=1;i<=n;i++) {
			for(int k=1;k<i;k++) {
				System.out.print(" ");
			}
			for (int j=(2*n+1);j>2*i;j--) {
				System.out.print("*");
			}
			System.out.println();
		}
		
	}

	public static void main(String[] args) {
		
		pattern9();

	}

}
