package stringPrograms;

public class RevString {
	
	static void revString(String str) {
		String rev = "";
		char ch [] = str.toCharArray();
		for(int i = ch.length-1; i>=0;i--) {
			rev = rev + ch[i];
		}
		System.out.println(rev);
	}
	
	public static void main(String[] args) {
		
		revString("Abhay");
		
	}

}
