package myPackage;

import java.util.Scanner;

public class PrimeNum {

	@SuppressWarnings("resource")
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter Num: ");
		int num = sc.nextInt();
		boolean isPrime = true;
		
		for (int i = 2;i<=num/2;i++) {
			if(num%i==0) {
				isPrime = false;
				break;
			}
		}
       if(isPrime) {
    	   System.out.println("Number is Prime");
       }else {
    	   System.out.println("Not Prime");
       }
	}
}
