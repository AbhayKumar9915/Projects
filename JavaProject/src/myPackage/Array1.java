package myPackage;

import java.util.Arrays;

public class Array1 {

	public static void main(String[] args) {
		int a[] = {4,5,3,8,1,7};
		int b[] = {2,6,3,7,4,5};
		int c[] = new int[5];
		
		
		for (int i =0; i<a.length-1;i++) {
			c[i] = a[i]+b[i+1];
			
		}
		System.out.println(Arrays.toString(c));
	}
}
