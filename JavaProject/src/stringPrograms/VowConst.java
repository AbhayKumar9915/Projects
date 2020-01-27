package stringPrograms;

public class VowConst {

	public static void main(String[] args) {
		
		int vCount = 0;
		int cCount = 0;
		String s = "I am String, found Vowels and Consonants in me";
		s = s.toLowerCase();
		
		for(int i=0;i<s.length();i++) {
			if(s.charAt(i)=='i' || s.charAt(i)=='a' || s.charAt(i)=='o' || s.charAt(i)=='u' || s.charAt(i)=='e') {
				vCount++;
			
			}else if(s.charAt(i)>'a' && s.charAt(i)<='z') {
				cCount++;
			}
		}
		System.out.println("Vowels Count: "+vCount);
		System.out.println("Consonants Count: "+cCount);

	}

}
