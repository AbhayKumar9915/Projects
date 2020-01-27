package myPackage;

import java.util.Arrays;
import java.util.HashSet;

public class ArrayCommonElements {

	public static void main(String[] args) {
		String [] array1 = {"Abhay","Ravi","Ruchi","Adarsh","Java","Python"};
		String [] array2 = {"Python","Ankit","Pankaj","Java","Match"};
		
		System.out.println("Array 1\n"+Arrays.toString(array1));
		System.out.println("Array 2\n"+Arrays.toString(array2));
		
		HashSet<String> set = new HashSet<String>();
		
		for(int i =0;i<array1.length; i++) {
			for (int j=0;j<array2.length;j++) {
				if(array1[i]==array2[j]) {
					set.add(array1[i]);
				}
			}
		}
		System.out.println("Common Element\n"+(set));
	}

}
