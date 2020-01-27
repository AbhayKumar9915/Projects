package serilizationConcept;

import java.io.*;

public class Desirealization {

	public static void main(String[] args) {
		
		try {
			
			FileInputStream fi = new FileInputStream("output1.txt");
			ObjectInputStream in = new ObjectInputStream(fi);
			
			Employee e1 = (Employee)in.readObject();
			Employee e2 = (Employee)in.readObject();
			Employee e3 = (Employee)in.readObject();
			
			System.out.println(e1.id+" "+e1.name);
			System.out.println(e2.id+" "+e2.name);
			System.out.println(e3.id+" "+e3.name);
			
			in.close();
			
		}catch(Exception e) {
			System.out.println(e);
		}

	}

}
