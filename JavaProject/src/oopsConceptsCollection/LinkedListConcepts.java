package oopsConceptsCollection;

import java.util.LinkedList;

public class LinkedListConcepts {

	public static void main(String[] args) {
		
		LinkedList <String>ll = new LinkedList<String>();
		ll.add("Abhay");
		ll.add("Ravi");
		ll.add("Adarsh");
		
		System.out.println(ll);
		ll.addFirst("First");
		ll.addLast("Last");
		System.out.println(ll);
		
		System.out.println(ll.get(2));
		ll.set(1, "Added");
		System.out.println(ll);
		
		ll.removeFirst();
		ll.removeLast();
		System.out.println(ll);
		
		ll.remove(1);
		System.out.println(ll);
		
		for (int i=0; i<ll.size();i++) {
			System.out.println(ll.get(i));
		}

	}

}
