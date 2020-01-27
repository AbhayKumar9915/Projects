package myPackage;

import java.util.Arrays;

public class SelectionSort {
	public static void sort(int[] a) {
		int temp;
		for(int i=0;i<a.length;i++) {
			int min = i;
			for(int j=i+1;j<a.length;j++) {
				if(a[j]<a[min]) {
					min = j;
				}
			}
			temp = a[i];
			a[i] = a[min];
			a[min]=temp;
		}
	}
	public static void main(String[] args) {
		int[] a = {4,1,10,-3,12};
		SelectionSort.sort(a);
	
		System.out.println(Arrays.toString(a));
	}

}
