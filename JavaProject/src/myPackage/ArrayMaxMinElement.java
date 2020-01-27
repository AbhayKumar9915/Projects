package myPackage;

//import java.util.Arrays;

public class ArrayMaxMinElement {
	public static int max(int array1[], int len) {
		int temp;
		for (int i =0;i<len;i++) {
			for (int j=i+1;j<len;j++) {
				if (array1[i]>array1[j]) {
					temp = array1[i];
					array1[i] = array1[j];
					array1[j] = temp;
				}
			}
		}
		return array1[len-1];
	}
	public static int min(int array1[], int len) {
		int temp;
		for (int i =0;i<len;i++) {
			for (int j=i+1;j<len;j++) {
				if (array1[i]<array1[j]) {
					temp = array1[i];
					array1[i] = array1[j];
					array1[j] = temp;
				}
			}
		}
		return array1[len-1];
	}

	public static void main(String[] args) {
		
		int [] array = {767,5433,125,365};
		
			System.out.println("Maximum Value in Array: "+max(array,4));
			System.out.println("Minimum Value in Array: "+min(array,4));
			
		}
	}
		



