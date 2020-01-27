package oopsConceptsCollection;

//Method Overriding and Inheritance, Subclass has the same method name declared in parent class.

class Bank{
	int getROI() {
		return 0;
	}
}
class SBI extends Bank{
	int getROI(){
		return 8;
	}
}
class ICICI extends Bank{
	int getROI(){
		return 7;
	}
}
class Axis extends Bank{
	int getROI(){
		return 9;
	}
}

public class MethodOverriding{

	public static void main(String[] args) {
		SBI s = new SBI();
		ICICI i = new ICICI();
		Axis a = new Axis();
		System.out.println("SBI ROI is: "+s.getROI());
		System.out.println("ICICI ROI is: "+i.getROI());
		System.out.println("Axis ROI is: "+a.getROI());
	}

}
