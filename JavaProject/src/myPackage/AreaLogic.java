package myPackage;

import java.util.Scanner;

public class AreaLogic
{   
	public static void main(String[] args) {
		@SuppressWarnings("resource")
		Scanner sc = new Scanner(System.in);
		System.out.println("You can calculate Area of Circle or Square, Enter 1 for Square and 2 for Circle");
		System.out.println("Enter your choice: ");
		int n = sc.nextInt();
		if(n==1) {
			System.out.println("Enter Radius: ");
			double r = sc.nextDouble();
			double A = Math.PI*r*r;
			System.out.println("Area of Circle is: "+A);
		}else if(n==2) {
			System.out.println("Enter Length of square: ");
			float l = sc.nextFloat();
			float A1 = l*l;
			System.out.println("Area of Square is: "+A1);
		}else {
			System.out.println("Invalid choice");
		}
	}
}