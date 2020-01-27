package com.guru99.testCases;
import org.testng.annotations.Test;
import com.guru99.pageObjects.LoginPage;

public class TC_LoginTest_001 extends BaseClass{
	
	@Test
	public void loginTest(){
		driver.get(baseURL);
		
		LoginPage lp = new LoginPage(driver);
		lp.setUserName(UserName);
		lp.setPassword(Password);
		lp.clickSubmit();
	}
	

}
