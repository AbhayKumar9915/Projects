package oopsConceptsCollection;

//Changing data type of arguments, If a class have multiple methods with same name but different parameters

public class MethodOverloading1 {
	static class Adder{
		static int add(int a, int b) {
			return a+b;
			}
		static double add(double a, double b) {
			return a+b;
			}
	}

	public static void main(String[] args) {
		System.out.println(Adder.add(5,25));
		System.out.println(Adder.add(26.44, 14.56846));

	}

}
