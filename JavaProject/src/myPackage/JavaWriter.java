package myPackage;
import java.io.*;

public class JavaWriter {

	public static void main(String[] args) {
		try {
			Writer wt = new FileWriter("File.txt");
			String content = "Hey Abhay!!\nThis is my First Example of Java File Writing";
			wt.write(content);
			wt.close();
			System.out.println("Done");
		}catch(Exception ex) {
			System.out.println(ex.getMessage());
		}

	}

}
