package oopsConceptsCollection;

//Changing number of arguments

public class MethodOverloading {
	static class Adder{
		static int add(int a, int b) {
			return a+b;
			}
		static int add(int a, int b, int c) {
			return a+b+c;
			}
	}

	public static void main(String[] args) {
		System.out.println(Adder.add(5,25));
		System.out.println(Adder.add(26, 14, 30));

	}

}
