package myPackage;

public class ExceptionH {

	@SuppressWarnings({ "null" })
	public static void main(String[] args) {
		try {
			String s =null;
			System.out.print(s.length());
			System.out.println("rest of the code"); 
		}catch(Exception e) {
			System.out.println(e);
		}
		try {
			int [] arr = new int[5];
			arr[6] = 10;
			
		}catch(Exception e) {
			System.out.println(e);
		}
		int data = 100/10;
		System.out.println(data);
	}

}
