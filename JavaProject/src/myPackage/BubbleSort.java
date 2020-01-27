package myPackage;

import java.util.Arrays;

public class BubbleSort {
	
	public static void sort(int[] a) {
		int temp;
		for(int i=0;i<a.length;i++) {
			for(int j=i+1;j<a.length;j++) {
				if(a[i]>a[j]) {
					temp = a[i];
					a[i] = a[j];
					a[j]=temp;
				}
			}
		}
	}
	public static void main(String[] args) {
		int[] a = {4,1,10,-3,12};
		BubbleSort.sort(a);
	
		System.out.println(Arrays.toString(a));
	}
}
