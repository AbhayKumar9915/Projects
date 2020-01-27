package oopsConceptsCollection;

import java.util.ArrayList;
import java.util.Iterator;

public class StudentArrayList {
	int rollno;
	String name;
	int age;
	StudentArrayList(int rollno,int age, String name){
		this.rollno =rollno;
		this.name = name;
		this.age = age;
	}
	
	public static void main(String[] args) {
		StudentArrayList s2 = new StudentArrayList(101,25,"Abhay");
		StudentArrayList s1 = new StudentArrayList(106,24,"Adarsh");
		StudentArrayList s3 = new StudentArrayList(111,26,"Ravi");
		
		ArrayList<StudentArrayList> AL = new ArrayList<StudentArrayList>();
		AL.add(s1);
		AL.add(s2);
		AL.add(s3);
		Iterator<StudentArrayList> itr = AL.iterator();
		while(itr.hasNext()) {
			StudentArrayList st = (StudentArrayList)itr.next();
			System.out.println("Roll Num: "+st.rollno+"| "+"Age: "+st.age+"| "+"Name: "+st.name);
		}
		
	}

}
