package oopsConceptsCollection;

//Multilevel inheritance (extends keyword used for inheriting parent class properties to child class)

class Employee{
	float salary = 40000;
}
class Bonus extends  Employee{
	int bonus = 10000;
}
public class Inheritance extends Bonus {

	public static void main(String[] args) {
		Inheritance it = new Inheritance();
		System.out.println("Employee Service is: "+it.salary);
		System.out.println("Bunus of employee is: "+it.bonus);

	}

}
