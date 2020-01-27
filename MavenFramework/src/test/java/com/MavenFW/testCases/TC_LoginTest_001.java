package com.MavenFW.testCases;
import org.testng.Assert;
import org.testng.annotations.Test;

import com.MavenFW.pageObjects.LoginPage;

public class TC_LoginTest_001 extends BaseClass{
	
	@Test(dataProvider = "LoginData")
	public void loginTest(String uname, String password) throws InterruptedException{
		LoginPage lp = new LoginPage(driver);
		lp.setUserName(uname);
		lp.setPassword(password);
		lp.clickLogin();
		Thread.sleep(2000);
		logger.info("User Logged in");
		lp.clickWelcomeAdmin();
		lp.clickLogout();
		Thread.sleep(2000);
		logger.info("User Logged out");
		
		if(driver.getTitle().equals("The Internet")) {
			Assert.assertTrue(true);
		}else {
			Assert.assertTrue(false);
		}
	}
	
}
