package ui;

import org.testng.annotations.AfterMethod;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

public class Annotations {
	
	@BeforeTest
	public void loginTest()
	{
		System.out.println("Login to application");
	}
	
	@AfterTest
	public void logoutTest()
	{
		System.out.println("Logout after all test");
	}
	
	@BeforeMethod
	public void connectDB()
	{
		System.out.println("DB connected");
	}
	
	@AfterMethod
	public void disconnectDB()
	{
		System.out.println("DB disconnected");
	}
	
	@Test(priority=2)
	public void test01()
	{
		System.out.println("First test is success");
	}
	
	@Test(priority=1)
	public void test02()
	{
		System.out.println("Second test is success");
	}
	
}
