package myPackage;

import java.util.Scanner;

public class EvenOddCount {
	

	public static void main(String[] args) {
		
		int eCount = 0,oCount=0;
		Scanner sc =  new Scanner(System.in);
		System.out.print("Enter Number: ");
		String num = sc.next();
		
		char [] arr = num.toCharArray();
		
		for(int i=0;i<num.length();i++) {
			if (arr[i]%2 == 0) {
				eCount++;
			}else {
				oCount++;
			}
		}
		System.out.println("Even Count: "+eCount);
		System.out.println("Odd Count: "+oCount);

		
	}

}
