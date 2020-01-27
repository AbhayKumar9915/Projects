package oopsConceptsCollection;

import java.util.HashMap;
import java.util.Map.Entry;

public class HashMap1 {

	public static void main(String[] args) {
		HashMap<String, String> hp = new HashMap<String, String>();
		
		hp.put("Name", "Abhay");
		hp.put("Compnay", "TCS");
		hp.put("State", "Karnataka");
		
		System.out.println(hp);
		hp.remove("State");
		
		for(Entry<String, String> m: hp.entrySet()) {
			System.out.println(m.getKey()+" "+m.getValue());
		}
		

	}

}
