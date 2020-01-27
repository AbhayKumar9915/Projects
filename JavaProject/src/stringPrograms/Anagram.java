package stringPrograms;

import java.util.Arrays;

public class Anagram {

	public static void main(String[] args) {
		
		String s1 = "Video";
		String s2 = "Dievo";
		
		s1 = s1.toLowerCase();
		s2 = s2.toLowerCase();
		
		if(s1.length() != s2.length()) {
			System.out.println("Can't be Anangram, not in equal size");
		}else {
			
			char[] s3 = s1.toCharArray();
			char[] s4 = s2.toCharArray();
			
			Arrays.sort(s3);
			Arrays.sort(s4);
			if(Arrays.equals(s3, s4) == true) {
				System.out.println("Anagram");
			}else {
				System.out.println("Not Anagram");
			}
			
		}

	}

}
