
package patternPrinting;

import java.util.Scanner;

public class Pattern8b {
	
public static void pattern8() {
		
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter number of iteration: ");
		int n = scan.nextInt();
		
		for(int i=1;i<=n;i++) {
			for (int k=n-1;k>=i;k--) {
				System.out.print(" ");
			}
			for (int j =1;j<(i*2);j++) {
				System.out.print("*");
			}
			
			System.out.println();
		}
		
}

	public static void main(String[] args) {
		
		pattern8();

	}

}
