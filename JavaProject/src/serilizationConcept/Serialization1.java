package serilizationConcept;

import java.io.*;

public class Serialization1 {

	public static void main(String[] args) {
		
		try {
			
			Employee E1 = new Employee(101,"Abhay");
			Employee E2 = new Employee(102,"Ravi");
			Employee E3 = new Employee(103,"Adarsh");
			
			FileOutputStream fout = new FileOutputStream(("output1.txt"));
			ObjectOutputStream oput = new ObjectOutputStream(fout);
			
			oput.writeObject(E1);
			oput.writeObject(E2);
			oput.writeObject(E3);
			
			oput.flush();
			oput.close();
			
			System.out.println("Serialization successfully done");
			
		}catch(Exception e) {
			System.out.println(e);
		}

	}

}
