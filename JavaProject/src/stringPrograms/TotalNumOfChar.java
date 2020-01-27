package stringPrograms;

public class TotalNumOfChar {

	public static void main(String[] args) {
		
		String s = "Hi Count Me";
		int count = 0;
		
		for(int i=0;i<s.length();i++) {
			if(s.charAt(i) != ' ') {
				count++;
			}
		
		}
		System.out.println(count);

	}

}
