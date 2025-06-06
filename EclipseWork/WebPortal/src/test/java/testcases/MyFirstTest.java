package testcases;

import org.openqa.selenium.By;
import org.testng.Assert;
import org.testng.annotations.Test;

import base.BaseTest;


public class MyFirstTest extends BaseTest{
	
	@Test
	public static void LoginTest() throws InterruptedException {
		String expected_title = "Zoho Home";
		driver.findElement(By.linkText(loc.getProperty("signin_link"))).click();
		Thread.sleep(2000);
		driver.findElement(By.id(loc.getProperty("email_id"))).sendKeys("abhayverma2010@gmail.com");
		driver.findElement(By.id(loc.getProperty("next_btn"))).click();
		Thread.sleep(2000);
		driver.findElement(By.id(loc.getProperty("password_id"))).sendKeys("Abhay@2010");
		driver.findElement(By.id(loc.getProperty("signin_btn"))).click();
		Thread.sleep(2000);
		String actual_title = driver.getTitle();
		Assert.assertEquals(actual_title, expected_title);

	}

}
