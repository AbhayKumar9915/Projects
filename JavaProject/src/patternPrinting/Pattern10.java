package patternPrinting;

import java.util.Scanner;

public class Pattern10 {
	
	public static void pattern10() {
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter Number: ");
		int n = sc.nextInt();
	    
		for(int i=1;i<=n;i++) {
			for(int j=1;j<=n;j++) {
				if(i>=2 && i<n && j>=2 && j<n) {
					System.out.print(" ");
				}else {
					System.out.print(i);
				}
				
			}
			System.out.println();
		}
	}

	public static void main(String[] args) {
		
		pattern10();

	}

}
